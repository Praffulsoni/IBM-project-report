from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

app = Dash(__name__)
data = pd.read_csv('dataset_part_1.csv')

app.layout = html.Div([
    html.H1('SpaceX Falcon 9 Landing Dashboard'),
    dcc.Dropdown(
        id='site',
        options=[{'label': s, 'value': s} for s in sorted(data['LaunchSite'].dropna().unique())],
        value=None,
        placeholder='Select launch site'
    ),
    dcc.Graph(id='payload-outcome')
])

@app.callback(Output('payload-outcome', 'figure'), Input('site', 'value'))
def update(site):
    d = data if site is None else data[data['LaunchSite'] == site]
    return px.scatter(d, x='PayloadMass', y='Class', color='Class',
                      title='Payload Mass vs Landing Outcome')

if __name__ == '__main__':
    app.run(debug=True)
