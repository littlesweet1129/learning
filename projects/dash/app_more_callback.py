# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate


external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    # dash state
    ## call back is only triggered when the state changes instead of input
    html.H2('Dash State', style={'textAlign': 'center'}),
    html.Div([
        dcc.Input(id='input-1-state', type='text', value='Montréal'),
        dcc.Input(id='input-2-state', type='text', value='Canada'),
        html.Button(id='submit-button', n_clicks=0, children='Submit'),
        html.Div(id='output-state')
    ]),
    html.Hr(),

    # PreventUpdate Exception
    html.H2('PreventUpdate Exception', style={'textAlign': 'center'}),
    html.Div([
        html.Button('Click here to see the content', id='button'),
        html.Div(id='body-div')
    ]),
    html.Hr(),

    # no update to update output partially
    html.H2('no update to update output partially', style={'textAlign': 'center'}),
    html.P('Enter a composite number to see its prime factors'),
    dcc.Input(id='num', type='number', debounce=True, min=1, step=1),
    html.P(id='err', style={'color': 'red'}),
    html.P(id='out')
])


@app.callback(
    Output("output-state", "children"),
    [Input('submit-button', 'n_clicks')],
    [State('input-1-state', 'value'),
    State('input-2-state', 'value')]
)
def update_output(n_clicks, input1, input2):
    return u'''
        The Button has been pressed {} times,
        Input 1 is "{}",
        and Input 2 is "{}"
    '''.format(n_clicks, input1, input2)

@app.callback(
    Output(component_id='body-div', component_property='children'),
    [Input(component_id='button', component_property='n_clicks')]
)
def update_output2(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else: 
        return "Elephants are the only animal that can't jump"

@app.callback(
    [Output('out', 'children'), Output('err', 'children')],
    [Input('num', 'value')]
)
def show_factors(num):
    if num is None:
        # PreventUpdate prevents ALL outputs updating
        raise dash.exceptions.PreventUpdate

    factors = prime_factors(num)
    if len(factors) == 1:
        # dash.no_update prevents any single output updating
        # (note: it's OK to use for a single-output callback too)
        return dash.no_update, '{} is prime!'.format(num)

    return '{} is {}'.format(num, ' * '.join(str(n) for n in factors)), ''

def prime_factors(num):
    n, i, out = num, 2, []
    while i * i <= n:
        if n % i == 0:
            n = int(n / i)
            out.append(i)
        else:
            i += 1 if i == 2 else 2
    out.append(n)
    return out

if __name__ == "__main__":
    app.run_server(debug=True)