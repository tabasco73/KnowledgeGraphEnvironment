# models.py

from typing import List, Optional
from pydantic import BaseModel, Field, field_validator
from enum import Enum

# Define Enums for constrained fields
class ArrowHead(str, Enum):
    normal = 'normal'
    odiamond = 'odiamond'
    diamond = 'diamond'
    box = 'box'

class Color(str, Enum):
    black = 'black'
    red = 'red'
    blue = 'blue'
    green = 'green'
    yellow = 'yellow'
    purple = 'purple'
    lightblue = 'lightblue'
    lightgreen = 'lightgreen'
    gray = 'gray'
    lightgray = 'lightgray'
    lightyellow = 'lightyellow'
    orange = 'orange'
    pink = 'pink'

class Shape(str, Enum):
    box = 'box'
    oval = 'oval'
    house = 'house'
    diamond = 'diamond'
    circle = 'circle'
    parallelogram = 'parallelogram'

# Model for individual nodes within a cluster
class Node(BaseModel):
    id: int
    label: str

    @field_validator('label')
    def label_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Label must not be empty')
        return v

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "label": "Model"
            }
        }

# Model for node clusters
class NodeCluster(BaseModel):
    name: str
    color: Color
    shape: Shape
    nodes: List[Node]

    @field_validator('nodes', mode='before')
    def validate_nodes(cls, v):
        if isinstance(v, list):
            transformed_nodes = []
            for idx, node_tuple in enumerate(v):
                if not isinstance(node_tuple, (list, tuple)) or len(node_tuple) != 2:
                    raise ValueError(f'Each node must be a tuple of (int, str), error at index {idx}')
                transformed_nodes.append({'id': node_tuple[0], 'label': node_tuple[1]})
            return transformed_nodes
        raise TypeError('nodes must be a list of tuples (int, str)')

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "name": "Models",
                "color": "lightgreen",
                "shape": "box",
                "nodes": [
                    {
                        "id": 1,
                        "label": "Model"
                    },
                    {
                        "id": 2,
                        "label": "(DGM) Directed Graphical Model"
                    }
                    # ... other nodes
                ]
            }
        }

# Model for connections within edges
class Connection(BaseModel):
    source: int
    targets: List[int]

    @field_validator('targets')
    def targets_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('Targets list must not be empty')
        return v

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "source": 1,
                "targets": [9]
            }
        }

# Model for edges
class Edge(BaseModel):
    color: Color
    connections: List[Connection]
    arrowhead: ArrowHead

    @field_validator('connections', mode='before')
    def validate_connections(cls, v):
        if isinstance(v, list):
            transformed_connections = []
            for idx, conn_tuple in enumerate(v):
                if not isinstance(conn_tuple, (list, tuple)) or len(conn_tuple) != 2:
                    raise ValueError(f'Each connection must be a tuple of (int, List[int]), error at index {idx}')
                transformed_connections.append({'source': conn_tuple[0], 'targets': conn_tuple[1]})
            return transformed_connections
        raise TypeError('connections must be a list of tuples (int, List[int])')

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "color": "black",
                "connections": [
                    {
                        "source": 1,
                        "targets": [9]
                    },
                    {
                        "source": 9,
                        "targets": [2, 63]
                    }
                    # ... other connections
                ],
                "arrowhead": "normal"
            }
        }

# Model for additional clusters in 'need_to_implement'
class AdditionalCluster(BaseModel):
    name: str
    color: Color
    nodes: Optional[List[int]] = []

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "name": "Datalänklagret",
                "color": "lightgray",
                "nodes": []
            }
        }

# Overall Graph Model
class GraphModel(BaseModel):
    nodes: List[NodeCluster]
    edges: List[Edge]
    clusters: List[AdditionalCluster]

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "nodes": [
                    # Example node clusters
                ],
                "edges": [
                    # Example edges
                ],
                "clusters": [
                    # Example additional clusters
                ]
            }
        }

def validate_graph(data: dict):
    try:
        graph = GraphModel(**data)
        print("Validation successful!")
        return graph
    except Exception as e:
        print(f"Validation error: {e}")
        raise