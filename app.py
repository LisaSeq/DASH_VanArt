#%%
from dash import dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

#%%
#Load the data
art_df = pd.read_csv("data/public-art.csv", sep=';')
art_df.head(10)
cities = list(art_df["Neighbourhood"].unique())
# %%

#Build our components
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
mytitle = dcc.Markdown(children = 'VanArt: Discover public Art')
mygraph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options = cities,
                        values='Downtown',
                        clearable=False)

#app.layout = html.Div('VanArt: Discover public Art')

#Customize layout


if __name__ == '__main__':
    app.run_server(debug = True)

dbc.Container()
# %%
