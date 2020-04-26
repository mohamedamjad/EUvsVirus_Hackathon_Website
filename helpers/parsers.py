import pandas as pd


def get_options(csv_path):
    options_list = []
    nodes = pd.read_csv(csv_path, index_col='id').columns
    for node in nodes:
        options_list.append({"label": node, "value": node})
    return options_list

def csv_line_to_edge(x, nodes_list, edges_list):
    for node in nodes_list:
        if x[node['data']['id']] == 1:
            edges_list.append({'data': {'source': x.name, 'target': node['data']['id']}, 'classes': 'one'})
        elif x[node['data']['id']] == -1:
            edges_list.append({'data': {'source': x.name, 'target': node['data']['id']}, 'classes': 'mone'})


def cytokines_parser(csv_path):
    nodes_list=[]
    edges_list=[]
    dataset = pd.read_csv(csv_path, index_col='id')
    # Parse nodes
    ids = dataset.columns
    for id in ids:
        nodes_list.append({'data': {'id': id, 'label': id}})
    # Parse edges
    dataset.apply(lambda x: csv_line_to_edge(x, nodes_list, edges_list), axis=1)

    return [nodes_list, edges_list]

#cytokines_parser('data/Model_lit_1.csv')
