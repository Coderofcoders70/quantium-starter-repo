from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__) # Initializing the dash app

df = pd.read_csv("formatted_data.csv")

df = df.sort_values(by="date")

# We use px as python.express to use plotly
fig = px.line(
    df, 
    x="date", 
    y="sales", 
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Total Sales ($)"}
)

app.layout = html.Div(children=[
    html.H1(
        children="Soul Foods: Pink Morsel Visualizer",
        style={"textAlign": "center", "color": "#2c3e50"}
    ),

    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)