from graphviz import Digraph

def help_fill(id_, name):
    return {"Id":f"{str(id_)}", "Info": f'ID:{id_} - {name}'}

def node_filler(list_id_names):
    nodes = []
    for id_, name in list_id_names:
        nodes.append(help_fill(id_, name))
    return nodes

def spread_edges(list1):
    spread = [(a, b) for a, b_s in list1 for b in b_s ]
    print(f'{spread=}')
    return spread

def node_add(dot, node_list, color_choice, fill_color,cluster_ids, **kwargs):
    clusters = {}
    for node in node_list:
        node_id = str(node["Id"])

        if node_id in cluster_ids:
            cluster_info = cluster_ids[node_id]
            cluster_name = 'cluster_' + cluster_info['name']
            cluster_color = cluster_info['color']

            if cluster_name not in clusters:
                clusters[cluster_name] = Digraph(name=cluster_name)
                clusters[cluster_name].attr(style='filled', color=cluster_color)
                
            clusters[cluster_name].node(node_id, label=node["Info"], color=color_choice, fillcolor=fill_color, **kwargs)
        else:
            dot.node(node_id, label=node["Info"], color=color_choice, fillcolor=fill_color, **kwargs)

    for cluster in clusters.values():
        dot.subgraph(cluster)

    return dot

def edge_add(dot, edges, nodes, color_choice, arrowhead):
    nodes = [int(node["Id"]) for node in nodes]
    for start, end in edges:
        #print(nodes)
        if start in nodes and end in nodes:
            #print(start in nodes)
            #print(f'{kwargs=}')
            print(f'{arrowhead}')
            dot.edge(str(start), str(end), color=color_choice, dir = 'back', arrowtail = arrowhead)
    return dot

def create_graph(nodes, edges, cluster_info = {}, filename = 'graph'):
    if cluster_info != {}:
        cluster_ids_ = transform_clusters(cluster_info)
    else:
        cluster_ids_ = {}
    nodes = transform_nodes(nodes)
    edges = transform_edges(edges)
    all_nodes = [node for node_set in nodes for node in node_set['nodes']]
    dot = Digraph(filename=filename, comment = 'Graphviz Diagram')
    for node_set_obj in nodes:
        dot = node_add(dot, node_set_obj['nodes'], node_set_obj['color'], node_set_obj['color'],cluster_ids_, style = 'filled', shape = node_set_obj['shape'])
    for edge_set_obj in edges:
        dot = edge_add(dot, edge_set_obj['edges'], all_nodes, edge_set_obj['color'], arrowhead = edge_set_obj['arrowhead'])
    dot.view()

def transform_nodes(nodes):
    return [
        {
            'name': node_obj['name'],
            'color': node_obj['color'],
            'shape': node_obj['shape'],
            'nodes': node_filler(node_obj['nodes'])
        } for node_obj in nodes
    ]

def transform_edges(edges):
    return [
        {
            'color': edge_obj['color'],
            'edges': spread_edges(edge_obj['connections']),
            'arrowhead': edge_obj['arrowhead']
        } for edge_obj in edges
    ]

def transform_clusters(cluster_info):
    cluster_ids_ = {str(a):{'name':cluster_info[0]['name'], 'color': cluster_info[0]['color']} for a in cluster_info[0]['nodes']}
    for iter, b in enumerate(cluster_info):
        if iter == 0:
            continue
        cluster_ids_.update({str(a): {'name':cluster_info[iter]['name'], 'color': cluster_info[iter]['color']} for a in cluster_info[iter]['nodes']})
    return cluster_ids_