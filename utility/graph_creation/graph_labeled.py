def spread_edges(list1):
    spread = []
    # Now handle both unlabeled and labeled targets
    for a, b_s in list1:
        for b in b_s:
            if isinstance(b, tuple) and len(b) == 2:
                # (target, label)
                target, label = b
                spread.append((a, target, label))
            else:
                # Just a target
                spread.append((a, b, None))
    return spread

def transform_edges(edges):
    return [
        {
            'color': edge_obj.get('color', 'black'),
            'arrowhead': edge_obj.get('arrowhead', 'normal'),
            'edges': spread_edges(edge_obj['connections']),
        }
        for edge_obj in edges
    ]

from graphviz import Digraph

def create_graph(nodes, edges, clusters, filename):
    dot = Digraph(comment='Knowledge Graph', format='png')

    # Add nodes
    for cluster in nodes:
        for node_id, node_name in cluster['nodes']:
            dot.node(str(node_id), node_name, shape=cluster['shape'], style='filled', fillcolor=cluster['color'])

    # Transform edges now (no need to do it beforehand)
    edges = transform_edges(edges)

    # Add edges
    for edge in edges:
        color = edge.get('color', 'black')
        arrowhead = edge.get('arrowhead', 'normal')
        for connection in edge['edges']:
            # connection is (source, target, label)
            a, b, label = connection
            if label:
                dot.edge(str(a), str(b), color=color, arrowhead=arrowhead, label=label)
            else:
                dot.edge(str(a), str(b), color=color, arrowhead=arrowhead)

    # Add clusters if any
    for cluster in clusters:
        with dot.subgraph(name='cluster_' + cluster['name']) as c:
            c.attr(style='filled', color=cluster['color'])
            for n in cluster['nodes']:
                c.node(str(n))
            c.attr(label=cluster['name'])

    dot.render(filename, view=True, cleanup=True)
