from utility.graph_creation.example_data import categories, edges, clusters

def transform_list(input_list):
    output_list = []
    for item in input_list:
        transformed_item = {
            'name': item['name'],
            'color': item['color'],
            'shape': item['shape'],
            'nodes': [(node['id'], node['name']) for node in item['nodes']]
        }
        output_list.append(transformed_item)
    return output_list

def transform_connections(input_list):
    output_list = []
    for item in input_list:
        transformed_item = {
            'color': item['color'],
            'connections': [(conn['id_from'], conn['ids_to']) for conn in item['connections']],
            'arrowhead': item['arrowhead']
        }
        output_list.append(transformed_item)
    return output_list

if __name__ == '__main__':
    print(transform_connections(edges))