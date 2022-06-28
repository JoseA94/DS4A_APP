import pandas as pd
import plotly.express as px  
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output





app = Dash(__name__)

# -- Import and clean data (importing csv into pandas)
#df = pd.read_csv("intro_bees.csv")
df = pd.read_csv("data/conteo_union.csv")


#print(df[:5])

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("DS4A TEAM 21 - La Asención", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "TOLIMA", "value": "TOLIMA"},
                     {"label": "BOGOTA D.C.", "value": 'BOGOTA D.C.'},
                     {"label": "ATLANTICO", "value": 'ATLANTICO'},
                     {"label": "VALLE DEL CAUCA", "value": '"VALLE DEL CAUCA'}],
                 multi=False,
                 value='TOLIMA',
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={})

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["Sucursal"] == option_slctd]
    #dff = dff[dff["Affected by"] == "Varroa_mites"]

    # Plotly Express

    fig = px.line(dff[(dff['Year_Month']!='NA')], x='Year_Month', y="Count_CCont")




    '''fig = px.choropleth(
        data_frame=dff,
        locationmode='USA-states',
        locations='state_code',
        scope="usa",
        color='Pct of Colonies Impacted',
        hover_data=['State', 'Pct of Colonies Impacted'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
        template='plotly_dark'
    )'''

    '''Plotly Graph Objects (GO)
    fig = go.Figure(
        data=[go.Choropleth(
            locationmode='USA-states',
            locations=dff['state_code'],
            z=dff["Pct of Colonies Impacted"].astype(float),
            colorscale='Reds',
        )]
    )

    fig.update_layout(
        title_text="Bees Affected by Mites in the USA",
        title_xanchor="center",
        title_font=dict(size=24),
        title_x=0.5,
        geo=dict(scope='usa'),
    )'''

    return container, fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    #app.run_server(debug=True)
    app.run(host='0.0.0.0', port=8050, debug=True)