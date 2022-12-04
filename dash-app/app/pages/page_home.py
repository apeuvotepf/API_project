import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State
from app.app_test import app

import sys
sys.path.append('../')
sys.path.append('../../')
from final_work.module.movie import Movie
from final_work.module.movie_facade import MovieFacade

pg = 'Movie search API'



def layout():
    return html.Div([dbc.Row(dbc.Col(dbc.Card(children=[
        dbc.CardHeader(html.H4(f'{pg.title()}', style={'textAlign': 'center'})),

        dbc.Row([
            dbc.Toast(
                [

                    dbc.Label("Enter the movie you want to search for :"),
                    dbc.Input(placeholder="Enter a movie here", type="text", id="movie_to_search_for"),
                    dbc.Button("Search", id="search_button", outline=True, color="primary", className="me-1", style={"margin-top":"5%"}),
            ],
                header="Movie search : ",
                header_class_name="bi bi-search",
                is_open=True,
                dismissable=False,                
            ),
            
            dbc.Row([
                html.Div(id="movies", 
                         style={"display": "flex", 
                                "flex-wrap": "wrap",
                                "justify-content":"space-around"}),
                ],
                style={"margin-top":"5%"}
            ),
            
            ],style={'margin': '2%'}
            ),

        


    ]),
        width={"size": 10, "offset": 1}))])


@app.callback(
    Output("movies", "children"),
    Input("search_button", "n_clicks"),
    State('movie_to_search_for', 'value'),
)
def get_movies_card(n_clicks, movie_to_search_for):

    if n_clicks==0:
        return []
    
    else:
        card_list = []
        
        if movie_to_search_for is not None:
            movies = MovieFacade.get_movies(movie_to_search_for)
            print(movies)
            if movies is not None:
                for movie in movies:
                    # assert isinstance(movie, Movie)
                    card = dbc.Card(
                            [
                                dbc.CardImg(src=movie.poster_url, top=True),
                                dbc.CardBody(
                                    [
                                        html.H4(movie.title, className="card-title"),
                                        html.P([
                                            movie.description,
                                            html.Br(),
                                            f"{str(movie.mean_rate)}"],
                                            className="card-text",
                                        ),
                                    ]
                                ),
                            ],
                            style={
                                "width": "15rem",
                                "margin-top":"5%",
                                }
                        )
                    card_list.append(card)
                return card_list
            else:
                
                alert = dbc.Alert(
                            [
                                html.I(className="bi bi-exclamation-triangle-fill me-2"),
                                html.P(["Your access to the API reaches its limits :(",
                                        html.Br(),
                                        "Retry tomorrow..."])
                            ],
                            color="danger",
                            className="d-flex align-items-center",
                        ),
                return alert
        
        else:
            return []