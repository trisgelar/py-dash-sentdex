import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash

APP = dash.Dash()

APP.layout = html.Div(children=[
    dcc.Input(
        id='input',
        value='Enter Something',
        type='text'
    ),
    html.Div(id='output')
])

# decorator / wrapper
@APP.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
    try:
        return str(float(input_data)**2)
        # "Input: {}".format(input_data)
    except:
        return "Some Error"


if __name__ == '__main__':
    APP.run_server(debug=True)
