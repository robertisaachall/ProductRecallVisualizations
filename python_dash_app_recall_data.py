import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import RecallDataSetupUtilities as rds

recall_data = pd.read_csv("data/recalls_recall_listing.csv")
recall_amount = rds.createOccurrencesCountries(recall_data)
recall_amount_type = rds.createRecallRemedyCountryData(recall_data, "China")
recall_columns = list(zip(*recall_amount))
recall_columns_type = list(zip(*recall_amount_type))

recall_data_AUS = pd.read_csv("data/Recall Action Result Summary Export - 20220412.csv")
recall_data_AUS = recall_data_AUS.iloc[0:6583, ]
recall_types_AUS = rds.create_recall_action_breakdown_AUS(recall_data_AUS)
recall_action_types_AUS = rds.create_recall_action_level_breakdown_AUS(recall_data_AUS)
recall_product_type_AUS = rds.create_recall_product_type_breakdown_AUS(recall_data_AUS)

recall_data_cars = pd.read_csv("data/FLAT_RCL_FLAT_RCL.csv", encoding='latin1')
car_recall_data_years = rds.create_car_recall_year_count(recall_data_cars).sort_values(by=['Year'])
car_recall_data_influence = rds.create_car_influenced_by_count(recall_data_cars)
car_recall_mfg = rds.create_car_mfg_count(recall_data_cars).sort_values(by=['Count'])

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
                html.H1(children=" Frequency for Each Location", className="graph_title"),
                html.P(
                    children="Individual product recall data based on individual countries and locations. Bar Graph "
                             "is interactive to view the data better.",
                    className="graph_description",
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
                html.H1(children=" Recall Type Breakdown by Location", className="graph_title"),
                html.P(
                    children=" Analyze the amount of product recalls based on the number of occurrences by country, "
                             "and the type of recall breakdown by country.",
                    className="graph_description",
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
        html.Div(
            children=[
                html.H1(children="Product Recall Analysis for Australia", className="header-title"),
                html.P(
                    children="Analyze the product recall breakdown for the country Australia, includes type "
                             "breakdown, the recall type and the specific product recalls.",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.H1(children=" Recall Type Breakdown Australia", className="graph_title"),
                html.P(
                    children="Analyze the amount of product recall types for Australia broken down into corresponding "
                             "sections regarding what type of recall was initiated.",
                    className="graph_description",
                ),
            ],
            className="third_graph",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(id='recall_pie_chart_aus',
                                       figure={
                                           "data": [
                                               {'x': recall_types_AUS.iloc[:, 0],
                                                'y': recall_types_AUS.iloc[:, 1], 'type': 'bar'}
                                           ]
                                       }),
                    className="card",
                ),
            ],
        ),
        html.Div(
            children=[
                html.H1(children=" Recall Type Breakdown Specific Product Type Australia",
                        className="graph_title"),
                html.P(
                    children=" Analyze the product recall type for the specific product recalled for Australia.",
                    className="graph_description",
                ),
            ],
            className="fourth_graph",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(id='recall_pie_chart_aus_product',
                                       figure={
                                           "data": [
                                               go.Pie(labels=recall_action_types_AUS.iloc[:, 0],
                                                      values=recall_action_types_AUS.iloc[:, 1])
                                           ]
                                       }),
                    className="card",
                ),
            ],
        ),
        html.Div(
            children=[
                html.H1(children=" Recall Type Breakdown Specific Product Type Australia",
                        className="graph_title"),
                html.P(
                    children=" Analyze the product recall type for the specific product recalled for Australia.",
                    className="graph_description",
                ),
            ],
            className="fifth_graph",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(id='recall_bar_chart_AUS',
                                       figure={
                                           "data": [
                                               go.Pie(labels=recall_product_type_AUS.iloc[:, 0],
                                                      values=recall_product_type_AUS.iloc[:, 1])

                                           ],
                                       }),
                    className="card",
                ),
            ],
        ),
        html.Div(
            children=[
                html.H1(children="Product Recall Analysis Car Recall", className="header-title"),
                html.P(
                    children="Analyze the product recall information for car recalls since 1969. Includes various "
                             "information about the recalls types and manufacturer.",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.H1(children=" Car Recall Data Amount per Year - CARS",
                        className="graph_title"),
                html.P(
                    children="Frequency over the year of recalls for specific car parts broken down into individual "
                             "years.",
                    className="graph_description",
                ),
            ],
            className="fifth_graph",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(id='recall_pie_chart_cars_year',
                                       figure={
                                           "data": [
                                               {'x': car_recall_data_years.iloc[:, 0],
                                                'y': car_recall_data_years.iloc[:, 1], 'type': 'bar'}
                                           ]
                                       }),
                    className="card",
                ),
            ],
        ),
        html.Div(
            children=[
                html.H1(children=" Car Recall Influenced by which Entity Graphs",
                        className="graph_title"),
                html.P(
                    children="Visualization of which specific entity initiated the car recall (OVSC,ODI,MFR)",
                    className="graph_description",
                ),
            ],
            className="fifth_graph",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(id='recall_bar_chart_cars_influence',
                                       figure={
                                           "data": [
                                               go.Pie(labels=car_recall_data_influence.iloc[:, 0],
                                                      values=car_recall_data_influence.iloc[:, 1])

                                           ],
                                       }),
                    className="card",
                ),
            ],
        ),
        html.Div(
            children=[
                html.H1(children=" Car Recall Count for Specific Manufacturers.",
                        className="graph_title"),
                html.P(
                    children="Number of instances each manufacturer has had a product recalled, filtered with "
                             "candidates above 600 instances.",
                    className="graph_description",
                ),
            ],
            className="fifth_graph",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(id='recall_chart_cars_mfg',
                                       figure={
                                           "data": [
                                               {'x': car_recall_mfg.iloc[:, 0],
                                                'y': car_recall_mfg.iloc[:, 1], 'type': 'bar'}
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
