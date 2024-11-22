from utility.graph_creation.graph_modules import create_graph
from utility.graph_creation.generate_cat_edges import create_graph_from_classes
from utility.graph_creation.utility import transform_connections, transform_list

from domains.pydantic.parkit_imports import classes_list


def get_ocpi_nodes():
    return [
    {
        'name': 'CommandObjects',
        'color': 'lightblue',
        'shape': 'box',
        'nodes': [
            (1, "CancelReservation"),
            (2, "ReserveNow"),
            (3, "StartSession"),
            (4, "StopSession"),
            (5, "UnlockConnector")
        ]
    },
    {
        'name': 'CommonFields',
        'color': 'lightgreen',
        'shape': 'ellipse',
        'nodes': [
            (6, "response_url"),
            (7, "token"),
            (8, "location_id"),
            (9, "evse_uid"),
            (10, "authorization_reference")
        ]
    },
    {
        'name': 'SpecificFields',
        'color': 'lightyellow',
        'shape': 'diamond',
        'nodes': [
            (11, "reservation_id"),
            (12, "expiry_date"),
            (13, "connector_id"),
            (14, "session_id")
        ]
    }
]

def get_edges():
    # Dependencies:
    #return [{'color': 'black', 'edges': [(5,[8,7]), (4,[3]), (3,[7])], 'arrowhead': 'normal'}]
    return 

def get_clusters():
    return [
    {
        'name': 'CommandModule',
        'color': 'lightgrey',
        'nodes': [1, 2, 3, 4, 5]
    }
]

clusters = [
    {
        'name': 'eMSPReceiver',
        'color': 'lightgrey',
        'nodes': [63, 64, 67, 73, 76, 70, 72, 75, 53, 56, 55, 97, 99, 100, 102, 104],  # Tariff, TariffElement, PriceComponent
    },
    {
        'name': 'CPOReceiver',
        'color': 'yellow',
        'nodes': [58, 65, 59, 71, 66, 74, 77, 54, 52, 57, 96, 98, 101, 103, 105 ],  # TariffType, TariffDimensionType, ReservationRestrictionType, DayOfWeek
    },
    {
        'name': 'Both',
        'color': 'blue',
        'nodes': [12, 14, 15, 16, 13, 17, 18, 23],  # TariffType, TariffDimensionType, ReservationRestrictionType, DayOfWeek
    },
]

def main_ocpi_min():
    categories, edges = create_graph_from_classes(classes_list, output_filename='docs/pydantic_graph_test_dot.png', layout_prog='dot')
    print(f'{len(categories)=}')
    print(f'{len(edges)=}')
    clusters = {}

    arrow_tails = ['normal', 'odiamond', 'diamond', 'box']
    colors = [ 'black', 'red', 'blue', 'green', 'yellow', 'purple', 'lightblue']
    dirs = ['back', 'both']
    #nodes = get_ocpi_nodes()
    #edges = get_edges()
    #clusters = get_clusters()
    filename = 'docs/ocpi_graph'
    nodes = transform_list(categories)
    edges = transform_connections(edges)
    """
    #Happyflow
    nodes = [
        {
            'name': 'eMSP implemented',
            'color': 'lightblue',
            'shape': 'ellipse',
            'nodes': [
                {'id': 1, 'name': 'GET - Locations - RECEIVER'},
                {'id': 2, 'name': 'PUT - Locations - RECEIVER'},
                {'id': 3, 'name': 'PATCH - Locations - RECEIVER'},
                {'id': 6, 'name': 'POST - Commands - SENDER'},
                {'id': 8, 'name': 'GET - Sessions - RECEIVER'},
                {'id': 9, 'name': 'PUT - Sessions - RECEIVER'},
                {'id': 10, 'name': 'PATCH - Sessions - RECEIVER'},
                {'id': 12, 'name': 'GET - CDRs - RECEIVER'},
                {'id': 13, 'name': 'POST - CDRs - RECEIVER'},
            ]
        },
        {
            'name': 'CPO implemented',
            'color': 'lightgreen',
            'shape': 'box',
            'nodes': [
                {'id': 4, 'name': 'GET - Locations - SENDERS'},
                {'id': 5, 'name': 'POST - Commands - RECEIVER'},
                {'id': 7, 'name': 'GET - Sessions - SENDER'},
                {'id': 11, 'name': 'GET - CDRs - SENDER'},
            ]
        },
    ]
    nodes = transform_list(nodes)
    edges = [
        {
            'color': 'black',
            'connections': [
                {'id_from': 4, 'ids_to': [3, 5]},
                {'id_from': 5, 'ids_to': [6]},
                {'id_from': 6, 'ids_to': [8]},
                {'id_from': 8, 'ids_to': [8]},
            ],
            'arrowhead': 'normal',
        },
    ]
    edges = transform_connections(edges)
    """
    clusters = {}
    print(f'{edges=}')
    print(f'{len(edges)=}')
    create_graph(nodes, edges, clusters, filename)
    #print(wrapper_gpt4(system_prompt, prompt))

if __name__ =='__main__':
    main_ocpi_min()