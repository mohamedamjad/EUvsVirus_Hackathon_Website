# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from components.jumbotron import jumbotron
from components.navbar import nav_bar
from components.cytoscape import cytoscape
from components.pdb import pdb
from dash.dependencies import Input, Output
from helpers.parsers import cytokines_parser

elements_list = cytokines_parser('data/Model_lit_1.csv')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'Cellgebra x UEvsVirus'
app.layout = html.Div(children=[
    nav_bar,
    jumbotron,
    cytoscape,
    pdb
])


@app.callback(
    Output(component_id='cytokines_view', component_property='elements'),
    [Input(component_id='select-cytokine', component_property='value')]
)
def update_cytokines_view(selected_value):
    print(selected_value)
    if((selected_value == None) | (selected_value == 'all')):
        return elements_list[0] + elements_list[1]
    return elements_list[0] + \
           list(filter(lambda x: True if ((x['data']['source'] == selected_value) | (x['data']['target'] == selected_value)) else False, elements_list[1]))


if __name__ == "__main__":
    app.run_server()