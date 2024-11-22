from utility.graph_creation.graph_modules import create_graph, transform_clusters, transform_edges, transform_nodes

arrow_tails = ['normal', 'odiamond', 'diamond', 'box']
colors = [ 'black', 'red', 'blue', 'green', 'yellow', 'purple', 'lightblue']
dirs = ['back', 'both']

def get_ocpi_nodes():
    return [{
        'name': 'Problem',
        'color': 'lightgreen',
        'shape': 'box',
        'nodes': [
            (3, "Optimization Problem"),
            (4, "(LP) Linear Programming Problem"),
            (17, "Optimization Problem; dual problem exists"),
            (18, "Dual Problem"),
            (40, "(TP) Transportation Problem"),
            ]
        },
        {
        'name': 'Methods',
        'color': 'lightblue',
        'shape': 'oval',
        'nodes': [
            (1, "Optimization Algorithm"),
            (2, "Simplex Method"),
            (19, "Algorithm"),
            (20, "Method"),
            (21, "Decision Rule"),
            (22, "Pivot-Based Algorithm"),
            (23, "Pivot Rule"),
            (24, "Dantzig's Rule"),

            ]
        },
        {
            'name': 'Function',
            'color': 'gray',
            'shape': 'house',
            'nodes': [
                (5, "Function"),
                (6, "Objective Function"),
                (7, "Linear Objective Function"),

                ]

        },
        {
            'name': 'Aggregation',
            'color': 'blue',
            'shape': 'diamond',
            'nodes': [
                (25, "Tensor"),
                (26, "Matrix"),
                (27, "Vector"),
                (28, "Constraint Matrix (A)"),
                (29, "Vector of decision variables (vec{x})"),
                (30, "Aggregation"),
                (31, "Set"),
                (32, "Basis of column space of Matrix"),
                (33, "Basis of column space of Constraint Matrix"),
                (34, "Vector in basis of column space of Constraint Matrix"),
                (35, "Basic Variable"),
                (36, "Solution to Optimization Problem"),
                (37, "Basic Solution"),
                (38, "Feasible Solution"),
                (39, "Basic Feasible Solution"),
                (41, "Initial Basic Feasible Solution"),


                
            ]
        },
        {
            'name': 'Variable',
            'color': 'orange',
            'shape': 'circle',
            'nodes': [
                (10, "Variable"),
                (11, "Auxiliary Variable"),
                (16, "Slack Variable"),
            ]
        },
        {
            'name': 'Condition',
            'color': 'purple',
            'shape': 'parallelogram',
            'nodes': [
                (8, "Equation"),
                (9, "Linear Equation"),
                (12, "Condition"),
                (13, "Constraint"),
                (14, "Linear Constraint"),
                (15, "LP constraint"),

            ]
        }

            
    ]

def get_edges():
    return [
        {
            'color':
                'black',
            'connections': [
                (19, [1]),
                (20, [19, 21]),
                (1, [2]),
                (3, [17, 18]),
                (17, [4]),
                (5, [6]),
                (6, [7]),
                (8, [9]),
                (9, [7]),
                (10, [11]),
                (11, [16]),
                (12, [8,13]),
                (13, [14]),
                (14, [15]),
                (15, [16]),
                (19, [22]),
                (22, [2]),
                (21, [23]),
                (23, [24]),
                (25, [26, 27]),
                (26, [28]),
                (27, [29]),
                (30, [31, 25, 36]),
                (31, [32]),
                (32, [33]),
                (27, [34]),
                (36, [37, 38]),
                (37, [39]),
                (38, [39]),
                (4, [40]),
                (39, [41]),
                
                

                ],
            'arrowhead': 'normal'

        },
        {
            'color':
                'black',
            'connections': [
                (4, [15, 7]),
                (17, [18]),
                (23, [22]),
                (15, [28, 29]),
                (33, [28]),
                (35, [34]),
                (34, [33]),
                (36, [3])
                ],
            'arrowhead': 'diamond'
        }
    ]

# I use this to represent subtypes that together make up all options of a type
def get_clusters():
    return [
        {
            'name': 'namn1',
            'color': 'lightgray',
            'nodes': []
        },
        {
            'name': 'namn2',
            'color': 'blue',
            'nodes': []
        },
    ]

def main_opt():
    nodes = get_ocpi_nodes()
    edges = get_edges()
    cluster = get_clusters()
    filename = 'docs/opt_graph'
    create_graph(nodes, edges, cluster, filename)

if __name__ =='__main__':
    main_opt()