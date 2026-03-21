from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__) # Initialize the app

df = pd.read_csv("formatted_data.csv")
df = df.sort_values(by="date")

app.layout = html.Div(style={'fontFamily': 'Arial, sans-serif', 'padding': '40px', 'backgroundColor': '#f9f9f9'}, children=[
    
    html.H1(
        children="Pink Morsel Sales Visualizer",
        style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': '30px'}
    ),

    html.Div(style={'textAlign': 'center', 'marginBottom': '20px'}, children=[
        html.Label("Select Region:", style={'fontWeight': 'bold', 'marginRight': '10px'}),
        dcc.RadioItems(
            id="region-filter",
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
            ],
            value='all', # Default selection
            inline=True,
            inputStyle={"margin-left": "20px", "margin-right": "5px"}
        )
    ]),

    html.Div(style={'backgroundColor': 'white', 'padding': '40px', 'borderRadius': '10px', 'boxShadow': '0px 4px 6px rgba(0,0,0,0.1)', 'margin': '0 auto', 'maxWidth': '1100px'}, children=[
        dcc.Graph(id="sales-line-chart")
    ])
])

# The Callback Logic
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):
    # Filter the data based on selection
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    # Create the updated figure
    fig = px.line(
        filtered_df, 
        x="date", 
        y="sales", 
        title=f"Pink Morsel Sales: {selected_region.title()} Region",
        labels={"date": "Date", "sales": "Total Sales ($)"},
        template="plotly_white"
    )

    fig.update_layout(
        margin=dict(l=60, r=20, t=50, b=50), 
        hovermode="x unified"                
    )
    
    # Smooth out the line appearance
    fig.update_traces(line_color='#3498db', line_width=2)
    
    return fig

if __name__ == "__main__":
    app.run(debug=True)