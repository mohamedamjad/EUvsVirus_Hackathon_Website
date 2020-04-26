import dash_bootstrap_components as dbc
import dash_html_components as html


jumbotron = dbc.Jumbotron(
    [
            html.H1("TACSS", className="display-3"),
            html.P(
                "Tackling cytokine storm syndrome in COVID-19 patients. "
                "Develop a data-driven mathematical model of cytokine storm syndrome to identify targets for drug re-positioning",
                className="lead"
            ),
            html.Hr(className="my-2"),
            html.P(
                "A significant proportion of  COVID-19 patients who develop severe disease appear to experience cytokine storm syndrome which is linked to high mortality rate.  The mechanism of cytokine storm is poorly understood, and development of new therapeutics is urgent. Several clinical trials are underway but success is not guaranteed. We are applying computational methods including data-driven network modelling and molecular modelling to the problem of drug repositioning for the treatment of cytokine storm in COVID-19 patients."
            ),
            html.P(dbc.Button("Learn more", color="dark", outline=True, href="https://devpost.com/software/tacking-cytokine-storm-syndrome-in-covid-19-patients"), className="lead")
    ], className="col-lg-6 col-md-6 col-sm-6 col-xs-12 offset-md-3 offset-sm-2 float-md-center"
)
