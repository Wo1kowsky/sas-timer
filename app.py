from datetime import date, time, datetime

import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

SAS_DISABLE_DATE = datetime(year=2022, month=10, day=1, hour=0)

app = dash.Dash()

app.layout = html.Div([
    dcc.Interval(id='timer-interval', interval=60 * 1000, n_intervals=0),
    html.Div(className='image'),
    html.Div(id='sas-message', children=[]),
], className='body')

# спринтов
# рабочих дней


@app.callback(Output('sas-message', 'children'),
              Input('timer-interval', 'n_intervals'))
def update_disable_message(n):
    current_datetime = datetime.now()
    days_remaining = (SAS_DISABLE_DATE - current_datetime).days
    if days_remaining % 10 == 1:
        days_word = 'день'
    elif days_remaining % 10 in (2, 3, 4):
        days_word = 'дня'
    else:
        days_word = 'дней'
    return html.Div([html.H1(f'{days_remaining} {days_word}'),
                     html.H3(f'До отключения SAS')],
                     # html.H3(f'{(SAS_DISABLE_DATE - current_datetime).days // 14} спринтов')],
                    style={'text-align': 'center'})


if __name__ == '__main__':
    app.run_server()
