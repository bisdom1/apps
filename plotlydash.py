# Generic
import pandas as pd 

# Plotly dash
import plotly.io as pio                     # plotly templates
import plotly.express as px 
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import flask

server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], server=server)

#### INIT DATA

pio.templates.default = "plotly_dark"
df = pd.read_csv('https://raw.githubusercontent.com/bisdom1/apps/master/assets/owid-covid-data.csv', na_values='nan') # read data in memory
df.date=pd.DatetimeIndex(df.date)
df.index=df.date
df['week'] = df.to_period('W').index.strftime("%Y-%m-%d")
df = df[df['continent'].notna()]
df = df[df['total_cases'].notna()]

#### LAYOUT

navbar = dbc.Navbar(
    children=[
        html.A(
            dbc.Row(
                [
                    dbc.Col(
                        dbc.NavbarBrand("\U0001F489 COVID-19 stats")
                    ),
                ],
                align="center",
                no_gutters=True,
            ),
            href="#",
        ),
    ],
    color="dark",
    dark=True,
    sticky="top",
    style={"height":"5vh"}
)

fig1 = px.scatter_geo(df, locations="iso_code", color="continent",
                     hover_name="location", size="total_cases",
                     animation_frame="week",
                     projection="equirectangular",
                     title='Total cases per country, coloured by continent',
                     size_max=50,
                     opacity=0.7,
                     template='plotly_dark')
fig1.update_layout(showlegend=False,height=900)
mapfig = dcc.Graph(figure=fig1, id='mapfig')

body = [
    html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Div(id='map-div',children=mapfig), width=9),
                dbc.Col(dbc.Spinner(html.Div(id='bar-div'),color='light'), width=3),
            ]
        ),
        dbc.Row(
            dbc.Col(
                [
                    dbc.Badge("\U0001F517 Data from ourworldindata.org", href="https://ourworldindata.org/coronavirus-source-data", color="light", className="mr-1"),
                ]
            )
        )
    ], style={'height':'94vh'}
)
]

content = html.Div(body, id="page-content")
app.layout = html.Div([navbar, content], style={'height':'100vh','overflow':'hidden',"background-color":"#000"})

#### CALLBACKS

@app.callback(
    Output('bar-div', 'children'),
    [Input('mapfig', 'hoverData')])
def display_hover_data(hoverData):
    if hoverData:
        country = hoverData['points'][0]['hovertext']
        fig2 = px.bar(df[df.location==country], x="date", y="new_cases", title="New cases per day in " + country,template='plotly_dark')
        fig2.update_layout(showlegend=False,height=900)
        barfig = dcc.Graph(figure=fig2)
        return barfig
    else:
        return dbc.Alert("Hover over a country to see the daily number of cases for that country", color='dark')  

if __name__ == "__main__":
    app.run_server(debug=True,host='0.0.0.0')