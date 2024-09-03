import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from data import get_server_metrics

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Server Monitoring Dashboard"),
    dcc.Interval(id='interval-component', interval=1000, n_intervals=0),
    html.Div(id='live-update-text')
])

@app.callback(Output('live-update-text', 'children'),
              Input('interval-component', 'n_intervals'))
def update_metrics(n):
    metrics = get_server_metrics()
    return [
        html.P(f"CPU Usage: {metrics['cpu']}%"),
        html.P(f"Memory Usage: {metrics['memory']}%"),
        html.P(f"Disk Usage: {metrics['disk']}%")
    ]

if __name__ == '__main__':
    app.run_server(debug=True)
