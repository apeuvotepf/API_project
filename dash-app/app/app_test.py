import dash
from dash import html, dcc
import dash_bootstrap_components as dbc


app = dash.Dash(__name__, url_base_pathname='/', suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])
server = app.server

app.layout = html.Div(children=[
    dcc.Location(id="url", refresh=False),
    html.Div(id="page-content")
])


if __name__ == '__main__':
    # Initialisation de l'app
    app.run_server(debug=True)
