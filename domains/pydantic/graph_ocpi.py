from utility.graph_creation.graph_modules import create_graph, transform_clusters, transform_edges, transform_nodes

arrow_tails = ['normal', 'odiamond', 'diamond', 'box']
colors = [ 'black', 'red', 'blue', 'green', 'yellow', 'purple', 'lightblue']
dirs = ['back', 'both']

def get_ocpi_nodes():
    return [{
        'name': 'functionalNodesReceiver',
        'color': 'lightblue',
        'shape': 'box',
        'nodes': [
                (7, "Commands"),
                (8, "ChargingProfiles"),
                (9, "Tokens"),
            ]
        },
        {
        'name': 'functionalNodesSender',
        'color': 'lightblue',
        'shape': 'oval',
        'nodes': [
                (3, "Locations"),
                (4, "Tariffs"),
                (5, "Sessions"),
                (6, "CDRs"),
            ]
        },
        {
        'name': 'configurationNodesBothForBoth',
        'color': 'gray',
        'shape': 'house',
        'nodes': [
                (1, "Version"),
                (2, "Credentials")
            ]
        },
        {
        'name': 'configurationNodesReceiver',
        'color': 'gray',
        'shape': 'circle',
        'nodes': [
                (10, "HubClientInfo")
            ]
        },
            
    ]

def get_edges():
    return [
        {
            'color': 'black',
            'connections': [
                (7,[5]),
                (5, [6])],
            'arrowhead': 'normal'
        }
    ]

def need_to_implement():
    return [
        {
            'name': 'connection',
            'color': 'red',
            'nodes': [1,2]
        },
        {
            'name': 'iteration1',
            'color': 'blue',
            'nodes': [5,6,7]
        },
        {
            'name': 'not_iteration1',
            'color': 'lightgray',
            'nodes': [3,4,8,9,10]
        }
    ]

def main_ocpi_graph():
    nodes = get_ocpi_nodes()
    edges = get_edges()
    cluster = need_to_implement()
    filename = 'ocpi_graph'
    create_graph(nodes, edges, cluster, filename)

if __name__ =='__main__':
    main_ocpi_graph