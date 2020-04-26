import dash_bootstrap_components as dbc
import dash_html_components as html

nav_bar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Open Source", href="https://github.com/cellgebra/EUvsVirus_Hackathon")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Research", header=True),
                dbc.DropdownMenuItem("paper 1", href="https://www.medrxiv.org/content/10.1101/2020.03.02.20029975v1"),
                dbc.DropdownMenuItem("paper 2", href="https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(20)30628-0/fulltext"),
                dbc.DropdownMenuItem("paper 3", href="https://europepmc.org/article/med/26854760"),
                dbc.DropdownMenuItem("link 2", href="https://link.springer.com/chapter/10.1007/978-3-319-30379-6_31")
            ],
            nav=True,
            in_navbar=True,
            label="Documentation"
        ),
    ],
    brand="Cellgebra",
    brand_href="#",
    color="dark",
    dark=True
)
