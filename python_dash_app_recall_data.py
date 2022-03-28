import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import RecallDataSetupUtilities as rds

recall_data = pd.read_csv("data/recalls_recall_listing.csv")
recall_amount = rds.createOccurrencesCountries(recall_data)
recall_amount_type = rds.createRecallRemedyCountryData(recall_data, "China")
recall_columns = list(zip(*recall_amount))
recall_columns_type = list(zip(*recall_amount_type))

external_stylesheets = [
    {
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(children="Product Recall Analysis", className="header-title"),
                html.P(
                    children="Analyze the amount of product recalls based on the number of occurrences by country, "
                             "and the type of recall breakdown by country.",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.H1(children=" Frequency for Each Location", className="first_graph_title"),
                html.P(
                    children=" Individual product recall data based on individual countries and locations. Bar Graph is interactive to view the data better.",
                    className="first_graph_description",
                ),
            ],
            className="first_graph",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(id='recall_bar_chart',
                                       figure={
                                           "data": [
                                               {'x': recall_columns[0], 'y': recall_columns[1], 'type': 'bar'}

                                           ],
                                       }),
                    className="card",
                ),
            ],
        ),
        html.Div(
            children=[
                html.H1(children=" Recall Type Breakdown by Location", className="second_graph_title"),
                html.P(
                    children=" Analyze the amount of product recalls based on the number of occurrences by country, "
                             "and the type of recall breakdown by country.",
                    className="second_graph_description",
                ),
            ],
            className="first_graph",
        ),
        html.Div(
            children=[
                html.Div(children="Region", className="menu-title"),
                dcc.Dropdown(
                    id="location-filter",
                    options=[
                        {"label": region, "value": region}
                        for region in recall_columns[0]
                    ],
                    value="COUNTRY",
                    clearable=False,
                    className="dropdown",
                ),
            ]
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(id='recall_pie_chart_country',
                                       figure={
                                           "data": [
                                               go.Pie(labels=recall_columns_type[0], values=recall_columns_type[1])
                                           ]
                                       }),
                    className="card",
                ),
            ],
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
