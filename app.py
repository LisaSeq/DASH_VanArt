#%%
from dash import dash, html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash.dash_table.Format import Format, Align

#%%
#Load the data
art_df = pd.read_csv("data/public-art.csv", sep=';').query('Status == "In place"')

# %%
#Build components
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

title = dcc.Markdown('# VanArt Lite: Discover public Art')

#Add graph
graph = dcc.Graph(figure = {})

#Add Dropdown options for Art Type and Neighbourhood
neighbourhoods = art_df["Neighbourhood"].dropna().unique().tolist()
art_types = art_df["Type"].dropna().unique().tolist()

dropdown1 = dcc.Dropdown(options = art_types,
                         value =['Mural', 'Figurative'],
                         clearable=False,
                         multi=True)
dropdown2 = dcc.Dropdown(options = neighbourhoods,
                         value =['Downtown', 'West End'],
                         clearable=False,
                         multi=True)

#Create Table
tbl_col_format = [ #Formatting columns to be included in table
    dict(id='Title of Work', name='Title of Art', format=Format()),
    dict(id='Type', name='Art Type', format=Format()),
    dict(id='Neighbourhood', name='Neighbourhood', format=Format()),
    dict(id='SiteAddress', name='Address', format=Format())
]

table = dash_table.DataTable(
    style_data={'whiteSpace': 'normal',
                'height': 'auto'},
                id='table',
                page_size=10,
                columns=tbl_col_format,  
                data=art_df.to_dict('records'),
            )

#Customize layout
app.layout = html.Div([title, dropdown1, dropdown2, graph, table])

#Customize layout
# app.layout = html.Div([mytitle,mygraph])
#     [dbc.row
#          html.H2("Title", className="diplay-4"),
#          html.Hr(),
#      dbc.Navbar(dropdown)
#      ]
#      )

#Callback for interactivity
@app.callback(
    Output(graph, component_property='figure'),
    Output(table, component_property='data'),
    Input(dropdown1, component_property='value'),
    Input(dropdown2, component_property='value')
)
def update_graph(art_type, neighbourhood):
    print(art_type)
    print(type(art_type))

    #Filter dataset based on user inputs
    data = art_df.loc[art_df["Type"].isin(art_type) & 
                      art_df["Neighbourhood"].isin(neighbourhood)]
    
    #Graph figure
    fig = px.bar(data, x="Neighbourhood", color = "Type", barmode = "stack")

    #Filter table
    tbl_data = data.to_dict('records')

    return fig, tbl_data

if __name__ == '__main__':
    app.run_server(debug = True)

