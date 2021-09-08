import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from app import app
from analitc import Analytics
import os
import webbrowser


webbrowser.open("http://127.0.0.1:8050/")


analy = Analytics()

input_file = dcc.Upload(
                    id='upload-data',
                    children=html.Div([
                        'Drag and Drop or ',
                        html.A('Select Files')
                    ]),
                    style={
                        'widht':'30%',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': '10px'
                    },
                    # Allow multiple files to be uploaded
                    multiple=True
                )

choose_lang = dcc.RadioItems(id='lang_chosen',
    options=[{'label':' Português   .', "value": 'por'},{'label':' Inglês ', "value": 'eng'}],
    value='por',
    labelStyle={}
)  


# Connect to the layout and callbacks of each tab
app.layout = dbc.Container([
    html.Div(html.Img(src='/assets/logo.jpeg', style={'height':'130px', 'width':'220px', "display": "block", 'margin-left': 'auto', 'margin-right': 'auto'})),
    html.Hr(),
    dbc.Row(dbc.Col(html.H1("Projeto para Inteligência Artificial 2",style={"textAlign": "center"}), width=12)),
    html.Hr(),

    dbc.Col([input_file, choose_lang], width=12),

    html.Div(
        [
        html.Br(),
        html.Div(id='output-image-upload'),
        html.Hr(),
        html.Pre('UFMA', style={'textAlign': 'center', 'margin': '10px'}),
        html.Pre('Alunos: Edno', style={'textAlign': 'center', 'margin': '10px'}),
    ],
    )

])

def parse_contents(contents):
    texto = analy.read(contents)
    path_audio = analy.say(texto)
    return dbc.Row([
                    dbc.Col([
                        html.H5('Imagem Analisada:'),
                        html.Br(),
                        html.Div(html.Img(src=contents, style={'height':'50%', 'width':'80%'})),
                    ],),
                    dbc.Col([
                        html.H5('Texto extraido da imagem:'), 
                        html.Audio(src=path_audio, controls=True),
                        html.Br(),
                        html.P(texto),
                    ],)
            ])


@app.callback([Output('output-image-upload', 'children')],
              [Input('upload-data', 'contents'), Input("lang_chosen", "value")],
              [State('upload-data', 'filename'),
              State('upload-data', 'last_modified')])

def update_output(list_of_contents, lang, list_of_names, list_of_dates):
    if list_of_contents is not None:
        analy.LANG = lang
        children = [parse_contents(c) for c, n, d in zip(list_of_contents, list_of_names, list_of_dates)]
        return children

if __name__=='__main__':
    app.run_server(debug=False)
