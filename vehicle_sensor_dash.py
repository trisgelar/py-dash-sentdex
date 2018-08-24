from collections import deque
import plotly.graph_objs as go
import random
import time
import dash_core_components as dcc
import dash_html_components as html
import dash

app = dash.Dash('vehicle-data')

max_length = 20
times = deque(maxlen=max_length)
oil_temps = deque(maxlen=max_length)
intake_temps = deque(maxlen=max_length)
coolant_temps = deque(maxlen=max_length)
rpms = deque(maxlen=max_length)
speeds = deque(maxlen=max_length)
throttle_pos = deque(maxlen=max_length)

data_dict = {
    "Oil Temperature":oil_temps,
    "Intake Temperature": intake_temps,
    "Coolant Temperature": coolant_temps,
    "RPM": rpms,
    "Speed": speeds,
    "Throttle Position": throttle_pos
}

def update_obd_values(times, oil_temps, intake_temps, coolant_temps, rmps, speeds, throttle_pos):
    times.append(time.time())
    if len(times) == 1:
        oil_temps.append(random.randrange(180,230))
        intake_temps.append(random.randrange(95,115))
        coolant_temps.append(random.randrange(170,200))
        rpms.append(random.randrange(1000,9500))
        speeds.append(random.randrange(30,140))
        throttle_pos.append(random.randrange(10,90))
    else:
        for data_of_interest in [oil_temps, intake_temps, coolant_temps, rmps, speeds, throttle_pos]:
            data_of_interest.append(data_of_interest[-1]+data_of_interest[-1]*random.uniform(-0.1,0.1))
            return times, oil_temps, intake_temps, coolant_temps, rmps, speeds, throttle_pos

times, oil_temps, intake_temps, coolant_temps, rmps, speeds, throttle_pos = update_obd_values(times, oil_temps, intake_temps, coolant_temps, rmps, speeds, throttle_pos)

layout = html.Div([
    html.Div([
        html.H2('Vehicle Data', style=dict(
            float='left'
        ))
    ]),
    dcc.Dropdown(
        id='vehicle-data-name',
        options=[dict(
            label=s,
            value=s
        ) for s in data_dict.keys()],
        value=['Coolant Temperature', 'Oil Temperature', 'Intake Temperature'],
        multi=True
    ),
    html.Div(children=html.Div(
        id='graphs',
    ), className='row'),
    dcc.Interval(
        id='graph-update',
        interval=100
    )
], className="container", style={
        'width':'98%',
        'margin-left':10,
        'margin-right':10,
        'max-width':50000
    })

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