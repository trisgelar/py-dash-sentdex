import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque

X = deque(maxlen=20)
Y = deque(maxlen=20)
X.append(1)
Y.append(1)

APP = dash.Dash(__name__)

APP.layout = html.Div([
    dcc.Graph(id='live-graph', animate=True),
    dcc.Interval(
        id='graph-update',
        interval=1000 #ms
    )
])

@APP.callback(
    Output('live-graph','figure'),
    events=[Event('graph-update','interval')]
)
def update_graph():
    global X
    global Y
    X.append(X[-1]+1)
    Y.append(Y[-1]+(Y[-1]*random.uniform(-0.1,0.1)))
    data = [go.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode='lines+markers'
    )]
    layout = go.Layout(
        title='My Live Graph',
        xaxis=dict(range=[min(X), max(X)]),
        yaxis=dict(range=[min(Y), max(Y)]),
    )
    return dict(data=data, layout=layout)

if __name__ == '__main__':
    APP.run_server(debug=True)
