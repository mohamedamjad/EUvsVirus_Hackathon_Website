import dash_bio as dashbio
import tempfile
import json
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_bio_utils import pdb_parser as parser, styles_parser as sparser


def files_data_style(content):
    fdat = tempfile.NamedTemporaryFile(suffix=".js", delete=False, mode='w+')
    fdat.write(content)
    dataFile = fdat.name
    fdat.close()
    return dataFile

fname = 'data/Figure-To-Manipulate.pdb'
# Create the model data from the decoded contents
modata = parser.create_data(fname)

fmodel = files_data_style(modata)

with open(fmodel) as fm:
    mdata = json.load(fm)

# Create the cartoon style from the decoded contents
datstyle = sparser.create_style(fname, 'cartoon', 'residue', **{})

fstyle = files_data_style(datstyle)
with open(fstyle) as sf:
    data_style = json.load(sf)

pdb = dbc.Card(
    [
        html.H4("Potential allosteric site of IP-10 (CXCL10) oligomer (PDB entry = 1O80).", className="card-title"),
        #html.H6("a subtitle about pdb file", className="card-subtitle"),
        html.P(
            "Our initial network analysis revealed that IP-10/CXCL10 might be a beneficial protein target for reducing cytokine storm in COVID-19 patients if inhibited by a small molecule for example. We have identified a potentially druggable allosteric site for follow-up in silico screening against compound databases (e.g. BindingDB - https://www.bindingdb.org/bind/index.jsp). Please feel free to manipulate the structure to gain more insight. ",
            className="card-text",
        ),
        html.Div(
            [
                dashbio.Molecule3dViewer(
                    id='molecule3d',
                    selectionType='atom',
                    modelData=mdata,
                    styles=data_style,
                    backgroundOpacity='0',
                    atomLabelsShown=False,
                )
            ],
            style={'width': '100%', 'height': '600px', 'border': 'solid 2px black'}
        ),
    ], className="col-lg-6 col-sm-12 offset-md-3 offset-sm-2 float-md-center shadow-lg p-3 mb-5 bg-white rounded", color='dark', outline=True
)
