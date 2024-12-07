from utility.graph_creation.graph_labeled import create_graph

arrow_tails = ['normal', 'odiamond', 'diamond', 'box']
colors = ['black', 'red', 'blue', 'green', 'yellow', 'purple', 'lightblue']
dirs = ['back', 'both']

def get_ocpi_nodes():
    return [
        {
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
    # Transform the previously dictionary-based edges into a tuple-based structure similar to opt.py,
    # but now including labels.
    # Format: (source, [(target, label), (target2, label2), ...])

    return [
        {
            'color': 'black',
            'arrowhead': 'normal',
            'connections': [
                (19, [(1, 'uses')]),
                (20, [(19, 'defines'), (21, 'includes')]),
                (1,  [(2, 'implements')]),
                (3,  [(17, 'has'), (18, 'has')]),
                (17, [(4, 'is dual to')]),
                (5,  [(6, 'defines')]),
                (6,  [(7, 'is')]),
                (8,  [(9, 'is a')]),
                (9,  [(7, 'relates to')]),
                (10, [(11, 'is')]),
                (11, [(16, 'is')]),
                (12, [(8, 'includes'), (13, 'includes')]),
                (13, [(14, 'is')]),
                (14, [(15, 'is')]),
                (15, [(16, 'relates to')]),
                (19, [(22, 'uses')]),
                (22, [(2, 'implements')]),
                (21, [(23, 'defines')]),
                (23, [(24, 'implements')]),
                (25, [(26, 'is a'), (27, 'is a')]),
                (26, [(28, 'defines')]),
                (27, [(29, 'defines'), (34, 'includes')]),
                (30, [(31, 'includes'), (25, 'includes'), (36, 'leads to')]),
                (31, [(32, 'defines')]),
                (32, [(33, 'defines')]),
                (36, [(37, 'results in'), (38, 'results in')]),
                (37, [(39, 'is a')]),
                (38, [(39, 'is a')]),
                (4,  [(40, 'leads to')]),
                (39, [(41, 'leads to')]),
            ]
        },
        {
            'color': 'black',
            'arrowhead': 'diamond',
            'connections': [
                (4,  [(15, 'relates to'), (7, 'involves')]),
                (17, [(18, 'is part of')]),
                (23, [(22, 'depends on')]),
                (15, [(28, 'uses'), (29, 'uses')]),
                (33, [(28, 'relates to')]),
                (35, [(34, 'relates to')]),
                (34, [(33, 'relates to')]),
                (36, [(3, 'is solution for')])
            ]
        }
    ]

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

def main_labeled_opt():
    nodes = get_ocpi_nodes()
    edges = get_edges()
    clusters = get_clusters()
    filename = 'docs/labeled_opt_graph'

    # Here we directly pass nodes, edges, and clusters to the labeled create_graph.
    # The graph_labeled.py create_graph function will handle labeled edges correctly.
    create_graph(nodes, edges, clusters, filename)

if __name__ == '__main__':
    main_labeled_opt()
