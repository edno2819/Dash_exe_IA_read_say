import dash
import dash_bootstrap_components as dbc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', dbc.themes.BOOTSTRAP, dbc.themes.YETI, dbc.themes.SUPERHERO]


app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[external_stylesheets[1]],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )