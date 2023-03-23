#%%
from dash import dash, html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash.dash_table.Format import Format, Align

#%%
#Load the data
art_df = pd.read_csv("../data/public-art.csv", sep=';').query('Status == "In place"')

#Setup app and layout/frontend
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])
server = app.server

#Build components
#Add graph
graph = dcc.Graph(figure = {})

#Add Dropdown options for Art Type and Neighbourhood
neighbourhoods = art_df["Neighbourhood"].dropna().unique().tolist()
art_types = art_df["Type"].dropna().unique().tolist()

dropdown1 = dcc.Dropdown(options = art_types,
                         value =['Mural', 'Figurative'],
                         clearable=False,
                         multi=True,
                         placeholder="Select an Art Type")
dropdown2 = dcc.Dropdown(options = neighbourhoods,
                         value =['Downtown', 'West End'],
                         clearable=False,
                         multi=True, 
                         placeholder="Select a Neighbourhood")

#Create Table
tbl_col_format = [ #Formatting columns to be included in table
    dict(id='Title of Work', name='Title of Art', format=Format()),
    dict(id='Type', name='Art Type', format=Format()),
    dict(id='Neighbourhood', name='Neighbourhood', format=Format()),
    dict(id='SiteAddress', name='Address', format=Format())
]

table = dash_table.DataTable(
    style_data={
    'whiteSpace': 'normal',
    'backgroundColor': 'rgb(255, 255, 255)',
    'color': 'rgb(0, 123, 167)',
    'height': 'auto'
    },
    id='table',
    page_size=10,
    columns=tbl_col_format,
    style_header={
    'backgroundColor': 'rgb(0, 123, 167)',
    'color': 'white'
    },
    style_cell={
        'fontFamily': 'Roboto, sans-serif',
        'textAlign': 'center',
    },
    data=art_df.to_dict('records')
    )

#Customize layout
app.layout = dbc.Container([
    html.H1(
    'VanArt Lite: Discover Public Art in Vancouver!', 
    style={
    'textAlign': 'center'
    }),
    html.Br(),
    html.Div(
    'This dashboard will help you explore the types of public art displays in Vancouver. \
        You can view a stacked bar graph showing what arts are available in what neigbourhoods and scroll \
            through the selected art and their locations in the table below.',
    style={
    'textAlign': 'justified', 'color': 'gray'
    }),
    html.Br(),
    dbc.Row([
        dbc.Col(["Select an Art Type"]),
        dbc.Col(["Select a Neighbourhood"])
        ]),
    dbc.Row([
        dbc.Col([dropdown1]),
        dbc.Col([dropdown2])
        ]),
    html.Br(),
    html.H4(
    'Section 1: Graph Displaying Art Type per Neighbourhood', 
    style={'textAlign': 'center'}
    ),
    graph,
    html.Br(), 
    html.H4(
    'Section 2: Table displaying details of Art selected', 
    style={'textAlign': 'center'}
    ),
    table
    ])

#Callback for interactivity
@app.callback(
    Output(graph, component_property='figure'),
    Output(table, component_property='data'),
    Input(dropdown1, component_property='value'),
    Input(dropdown2, component_property='value')
)
def update_graph_table(art_type, neighbourhood):
    print(art_type)
    print(type(art_type))

    #Filter dataset based on user inputs
    data = art_df.loc[art_df["Type"].isin(art_type) & 
                      art_df["Neighbourhood"].isin(neighbourhood)]
    
    #Graph figure
    fig = px.bar(data, 
                 x="Neighbourhood", 
                 color = "Type", 
                 barmode = "stack"
                 )

    #Filter table
    tbl_data = data.to_dict('records')

    return fig, tbl_data

if __name__ == '__main__':
    app.run_server(debug = True)
# %%
