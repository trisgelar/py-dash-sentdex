import dash_core_components as dcc
import dash_html_components as html
import dash

APP = dash.Dash()

APP.layout = html.Div(
    children=[
        html.H1('Dash tutorials'),
        dcc.Graph(
            id='example',
            figure=dict(
                data=[
                    dict(
                        x=[1,2,3,4,5],
                        y=[5,6,7,2,1],
                        type='line',
                        name='boats'
                    ),
                    dict(
                        x=[1,2,3,4,5],
                        y=[8,3,2,3,5],
                        type='bar',
                        name='cars'
                    ),
                ],
                layout=dict(
                    title='Basic Dash Example'
                )
            )
        )
    ])

if __name__ == '__main__':
    APP.run_server(debug=True)
