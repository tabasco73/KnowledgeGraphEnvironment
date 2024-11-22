from pydantic import BaseModel, Field # type: ignore
from typing import List, Type, Union, Optional, get_type_hints
from enum import Enum
import pygraphviz as pgv # type: ignore
import inspect
from domains.pydantic.parkit_imports import classes_list

# Define styles for different relationship types
RELATIONSHIP_STYLES = {
    'attribute': {'color': 'brown', 'style': 'solid'},
    'list_attribute': {'color': 'blue', 'style': 'dashed'},
    'optional_attribute': {'color': 'green', 'style': 'dotted'},
    'optional_list_attribute': {'color': 'purple', 'style': 'dashed'}
}

# Define a mapping from keyword to color
KEYWORD_COLOR_MAP = {
    'session': 'orange',
    'cdr': 'blue',
    'command': 'pink',
    'version': 'brown',
    'credential': 'green',
    'location': 'purple',
    'tokens': 'yellow',

}

def create_graph_from_classes(classes: List[Type[Union[BaseModel, Enum]]], output_filename: str = 'pydantic_graph.png', layout_prog: str = 'dot'):
    graph = pgv.AGraph(strict=False, directed=True)
    edge_set = set()
    for model in classes:
        create_graph_from_pydantic(model, graph, edge_set)
    categories = generate_categories(graph)
    edges = generate_edges(graph, categories)
    
    # Output the graph
    graph.layout(prog=layout_prog)
    graph.draw(output_filename)
    print(f"Number of nodes: {len(graph.nodes())}, {len(categories)}")
    print(f"Number of edges: {len(graph.edges())}, {len(edges)}")
    return categories, edges

def create_graph_from_pydantic(model: Type[Union[BaseModel, Enum]], graph=None, edge_set=None):
    model_name = model.__name__.lower()  # Use lowercase for consistent matching
    # Check for HTTP method keywords and determine color based on additional keywords
    node_color = None
    if any(action in model_name for action in ["get", "put", "patch", "post"]):
        for keyword, color in KEYWORD_COLOR_MAP.items():
            if keyword in model_name:
                node_color = color
                print(f"Node '{model.__name__}' contains HTTP method and '{keyword}', and will be colored {color}.")
                break
    if not node_color:
        # Default colors if no specific keyword is matched
        node_color = "lightyellow" if issubclass(model, BaseModel) else "lightgrey"
        node_pen_color = "lightblue" if issubclass(model, BaseModel) else "red"
    else:
        node_pen_color = node_color
    # Distinguish nodes based on type
    if issubclass(model, BaseModel):
        graph.add_node(model.__name__, shape="ellipse", style="filled", fillcolor=node_color, color=node_pen_color, penwidth=2)
    elif issubclass(model, Enum):
        graph.add_node(model.__name__, shape="box", style="filled", fillcolor=node_color, color=node_pen_color, penwidth=2)
    if issubclass(model, BaseModel):
        for name, field in model.__annotations__.items():
            field_type = get_type_hints(model)[name]
            types_to_handle = []
            if hasattr(field_type, "__origin__"):
                if field_type.__origin__ in {Union, Optional}:
                    for sub_type in field_type.__args__:
                        if hasattr(sub_type, "__origin__") and sub_type.__origin__ == list:
                            types_to_handle.append((sub_type.__args__[0], 'optional_list_attribute'))
                        else:
                            types_to_handle.append((sub_type, 'optional_attribute'))
                elif field_type.__origin__ == list:
                    types_to_handle.append((field_type.__args__[0], 'list_attribute'))
            else:
                types_to_handle.append((field_type, 'attribute'))
            for sub_type, relationship_type in types_to_handle:
                if inspect.isclass(sub_type):
                    handle_field_type(sub_type, model.__name__, graph, edge_set, relationship_type)
    return graph

def handle_field_type(field_type, model_name, graph, edge_set, relationship_type):
    """Handles the creation of edges and nodes for a given field type."""
    if issubclass(field_type, BaseModel):
        if not graph.has_node(field_type.__name__):
            graph.add_node(field_type.__name__, shape="ellipse", style="filled", fillcolor="lightyellow", color="lightyellow", penwidth=2)
        if (model_name, field_type.__name__) not in edge_set:
            graph.add_edge(model_name, field_type.__name__, **RELATIONSHIP_STYLES[relationship_type])
            edge_set.add((model_name, field_type.__name__))
        create_graph_from_pydantic(field_type, graph, edge_set)
    elif issubclass(field_type, Enum):
        if not graph.has_node(field_type.__name__):
            graph.add_node(model_name, shape="box", style="filled", fillcolor="lightblue", color="lightblue", penwidth=2)
        if (model_name, field_type.__name__) not in edge_set:
            graph.add_edge(model_name, field_type.__name__, **RELATIONSHIP_STYLES[relationship_type])
            edge_set.add((model_name, field_type.__name__))

def generate_categories(graph):
    """Generates the categories structure from the graph."""
    categories = []
    node_id = 0 
    for node in graph.nodes():
        node_data = {
            'name': node,
            'color': graph.get_node(node).attr.get('color', 'lightblue') or 'lightblue',
            'shape': graph.get_node(node).attr.get('shape', 'ellipse') or 'ellipse',
            'nodes': [{'id': node_id, 'name': node}]
        }
        categories.append(node_data)
        node_id += 1
    return categories

def generate_edges(graph, categories):
    """Generates the edges structure from the graph."""
    edges = []
    for edge in graph.edges():
        u, v = edge
        u_id = next((category['nodes'][0]['id'] for category in categories if category['name'] == u), None)
        v_id = next((category['nodes'][0]['id'] for category in categories if category['name'] == v), None)

        if u_id is not None and v_id is not None:
            connection_data = {
                'color': graph.get_edge(u, v).attr.get('color', 'orange') or 'orange',
                'arrowhead': graph.get_edge(u, v).attr.get('arrowhead', 'normal') or 'normal',
                'connections': [{
                    'id_from': u_id,
                    'ids_to': [v_id]
                }]  # Store the connection as a dictionary
            }
            edges.append(connection_data)
    return edges

if __name__ == '__main__':
    categories, edges = create_graph_from_classes(classes_list, output_filename='pydantic_graph_test_dot.png', layout_prog='dot')
    # You can now run the tests using the generated categories and edges
    print(f'{categories=}')
    print(f'{edges=}')
    print(f'{len(categories)=}')
    print(f'{len(edges)=}')
