import dash_bootstrap_components as dbc
from dash import html, dcc


def define_layout(pg_name):
    return html.Div([dbc.Row(dbc.Col(dbc.Card(children=[
        dbc.CardHeader(html.H4(f'{pg_name.title()} page', style={'textAlign': 'center'})),
        dbc.CardBody(children=[
            dcc.Link(children="Link to home page", href="/"), html.Br(),
        ])
    ]), width={"size": 10, "offset": 1}))])
