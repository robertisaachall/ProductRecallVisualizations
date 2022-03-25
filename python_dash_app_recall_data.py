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

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Product Recall Analysis"),
    html.P("Analyze the amount of product recalls based on the number of occurrences by country, and the type of recall breakdown by country."),

    html.H1("Product Recall Based on Individual Locations"),
    html.P("Individual product recall data based on inidivudal countries and locations. Bar Graph is interactive to view the data better."),
    dcc.Graph(id='recall_bar_chart',
              figure={
                  "data": [
                      {'x': recall_columns[0], 'y': recall_columns[1], 'type': 'bar'}

                  ],
              }),

    html.H1("Product Recall Type on Specified Location"),
    html.P("Product Recall Type information (Refund, Replace, Repair, etc) for the specified country or location."),
    dcc.Graph(id='recall_pie_chart_country',
              figure={
                  "data": [
                      go.Pie(labels=recall_columns_type[0], values= recall_columns_type[1])
                  ]
              })
])




if __name__ == "__main__":
    app.run_server(debug=True)
