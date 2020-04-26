import dash_cytoscape as cyto
import dash_html_components as html
from helpers.parsers import get_options
import dash_bootstrap_components as dbc

cytoscape = dbc.Card(
    [
        html.H4("Cytokines interaction", className="card-title"),
        #html.H6("a deep dive into cytokines interaction", className="card-subtitle"),
        html.P(
            "Interactions between cytokines upregulated in COVID-19 patients as described in the literature.",
            className="card-text",
        ),
        dbc.Select(
            id="select-cytokine",
            options=[{"label": "All", "value": "all"}] + get_options('data/Model_lit_1.csv'),
            style={
                'margin': '10px',
                'width': '40%'
            }
        ),
        cyto.Cytoscape(
            id='cytokines_view',
            layout={'name': 'circle'},
            style={'width': '100%', 'height': '600px', 'border': 'solid 2px black'},
            elements=[],
            stylesheet=[
                {
                    'selector': 'node',
                    'style': {
                        'content': 'data(label)'
                    }
                },
                {
                    'selector': 'edge',
                    'style': {
                        # The default curve style does not work with certain arrows
                        'curve-style': 'bezier'
                    }
                },
                {
                    'selector': '.one',
                    'style': {
                        'target-arrow-color': 'green',
                        'target-arrow-shape': 'triangle',
                        'line-color': 'green'
                    }
                },
{
                    'selector': '.mone',
                    'style': {
                        'target-arrow-color': 'red',
                        'target-arrow-shape': 'tee',
                        'line-color': 'red'
                    }
                }
            ],
        ),
        html.P(dbc.Button("Simulation", color="dark", outline=True, href="https://drive.google.com/file/d/1EWeLCVKWfqntN3SF6PyI32Y2Yi7CKSS3/view?usp=sharing"), className="lead")
    ], className="col-lg-6 col-sm-12 offset-md-3 offset-sm-2 float-md-center shadow-lg p-3 mb-5 bg-white rounded", color='dark', outline=True
)