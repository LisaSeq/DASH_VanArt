#%%
from dash import dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

#%%
#Load the data
art_df = pd.read_csv("data/public-art.csv", sep=';').query('Status == "In place"')
neighbourhoods = list(art_df["Neighbourhood"].unique())
art_types = list(art_df["Type"].unique())

# %%
#Build our components
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

title = dcc.Markdown('# VanArt: Discover public Art')
graph = dcc.Graph(figure = {})
dropdown1 = dcc.Dropdown(options = art_types,
                         value =['Mural'],
                         clearable=False,
                         multi=True)
dropdown2 = dcc.Dropdown(options = neighbourhoods,
                         value ='Downtown',
                         clearable=False,
                         multi=True)

#Customize layout
app.layout = html.Div([title,dropdown1, graph, dropdown2])

#Customize layout
#app.layout = html.Div([mytitle,mygraph])
    # [
    #     html.H2("Title", className="diplay-4"),
    #     html.Hr(),
    # dbc.Navbar(dropdown)
    # ]
    # )

#Callback for interactivity
@app.callback(
    Output(graph, component_property='figure'),
    Input(dropdown1, component_property='value')
)
def update_graph(art_type):
    print(art_type)
    print(type(art_type))

    #Filter dataset based on user inputs
    data = art_df.loc[art_df["Type"].isin(art_type)]
    
    #Graph figure
    fig = px.bar(data, x="Neighbourhood", color = "Type", barmode = "stack")
    return fig

if __name__ == '__main__':
    app.run_server(debug = True)

