# List of categories with associated nodes
categories = [
    {
        'name': 'Locations',         
        'color': 'lightblue',       
        'shape': 'ellipse',       
        'nodes': [                      
            {'id': 1, 'name': 'Location'},  
            {'id': 2, 'name': 'EVSE'},  
            {'id': 3, 'name': 'Connector'},  
        ]
    },
    {
        'name': 'Interfaces',         
        'color': 'lightgreen',       
        'shape': 'box',       
        'nodes': [                      
            {'id': 4, 'name': 'Sender Interface'},  
            {'id': 5, 'name': 'Receiver Interface'},  
        ]
    },
    {
        'name': 'Methods',         
        'color': 'lightcoral',       
        'shape': 'box',       
        'nodes': [                      
            {'id': 6, 'name': 'GET'},  
            {'id': 7, 'name': 'PUT'},  
            {'id': 8, 'name': 'PATCH'},  
        ]
    },
]

# List of edges connecting nodes, create different objects for different edge types.
edges = [
    {
        'color': 'black',            
        'connections': [                     
            {'id_from': 1, 'ids_to': [2]},   
            {'id_from': 2, 'ids_to': [3]},   
        ],
        'arrowhead': 'normal',    
    },
    {
        'color': 'blue',            
        'connections': [                     
            {'id_from': 4, 'ids_to': [1, 2, 3]},   
            {'id_from': 5, 'ids_to': [1, 2, 3]},   
        ],
        'arrowhead': 'vee',    
    },
    {
        'color': 'red',            
        'connections': [                     
            {'id_from': 6, 'ids_to': [1, 2, 3]},   
            {'id_from': 7, 'ids_to': [1, 2, 3]},   
            {'id_from': 8, 'ids_to': [1, 2, 3]},   
        ],
        'arrowhead': 'vee',    
    },
]

# List of clusters with associated nodes
clusters = [
    {
        'name': 'LocationCluster',           
        'color': 'lightgrey',        
        'nodes': [1, 2, 3],        
    },
    {
        'name': 'InterfaceCluster',           
        'color': 'lightyellow',        
        'nodes': [4, 5],        
    },
    {
        'name': 'MethodCluster',           
        'color': 'lightpink',        
        'nodes': [6, 7, 8],        
    },
]

categories = [
        {
            'name': 'Tariff Components',
            'color': 'lightblue',
            'shape': 'ellipse',
            'nodes': [
                {'id': 1, 'name': 'Tariff'},
                {'id': 2, 'name': 'TariffElement'},
                {'id': 3, 'name': 'PriceComponent'},
            ]
        },
        {
            'name': 'Enums',
            'color': 'lightgreen',
            'shape': 'box',
            'nodes': [
                {'id': 4, 'name': 'TariffType'},
                {'id': 5, 'name': 'TariffDimensionType'},
                {'id': 6, 'name': 'ReservationRestrictionType'},
                {'id': 7, 'name': 'DayOfWeek'},
            ]
        },
        {
            'name': 'Restrictions',
            'color': 'lightcoral',
            'shape': 'box',
            'nodes': [
                {'id': 8, 'name': 'TariffRestrictions'},
            ]
        },
    ]

edges = [
    {
        'color': 'black',
        'connections': [
            {'id_from': 1, 'ids_to': [2]},   # Tariff -> TariffElement
            {'id_from': 2, 'ids_to': [3]},   # TariffElement -> PriceComponent
        ],
        'arrowhead': 'normal',
    },
    {
        'color': 'blue',
        'connections': [
            {'id_from': 3, 'ids_to': [5]},   # PriceComponent -> TariffDimensionType (Enum)
            {'id_from': 2, 'ids_to': [6]},   # TariffElement -> ReservationRestrictionType (Enum)
            {'id_from': 8, 'ids_to': [7]},   # TariffRestrictions -> DayOfWeek (Enum)
        ],
        'arrowhead': 'vee',
    },
    {
        'color': 'red',
        'connections': [
            {'id_from': 1, 'ids_to': [8]},   # Tariff -> TariffRestrictions
        ],
        'arrowhead': 'vee',
    },
]

clusters = [
    {
        'name': 'TariffCluster',
        'color': 'lightgrey',
        'nodes': [1, 2, 3],  # Tariff, TariffElement, PriceComponent
    },
    {
        'name': 'EnumCluster',
        'color': 'lightyellow',
        'nodes': [4, 5, 6, 7],  # TariffType, TariffDimensionType, ReservationRestrictionType, DayOfWeek
    },
    {
        'name': 'RestrictionCluster',
        'color': 'lightpink',
        'nodes': [8],  # TariffRestrictions
    },
]

[{'color': 'black', 'connections': [{'id_from': 1, 'ids_to': [2]}], 'arrowhead': 'normal'}, {'color': 'black', 'connections': [{'id_from': 1, 'ids_to': [3]}], 'arrowhead': 'normal'}, {'color': 'black', 'connections': [{'id_from': 1, 'ids_to': [4]}], 'arrowhead': 'normal'}, {'color': 'black', 'connections': [{'id_from': 4, 'ids_to': [5]}], 'arrowhead': 'normal'}, {'color': 'black', 'connections': [{'id_from': 5, 'ids_to': [6]}], 'arrowhead': 'normal'}, {'color': 'black', 'connections': [{'id_from': 4, 'ids_to': [7]}], 'arrowhead': 'normal'}]
[{'name': 'TariffCluster', 'color': 'lightgrey', 'nodes': [1]}, {'name': 'PriceCluster', 'color': 'lightgrey', 'nodes': [3]}, {'name': 'TariffElementCluster', 'color': 'lightgrey', 'nodes': [4]}, {'name': 'PriceComponentCluster', 'color': 'lightgrey', 'nodes': [5]}, {'name': 'RestrictionsCluster', 'color': 'lightpink', 'nodes': [8]}]