import dash
from dash import dcc, html  # ✅ modern import style

# CREATING A DASH APPLICATION
app = dash.Dash(__name__)

# DEFINE THE LAYOUT OF THE DASHBOARD
app.layout = html.Div(
    children=[
        html.H1('MY DASHBOARD'),
        dcc.Graph(
            id='My-Graph',
            figure={
                'data': [  # ✅ 'Data' → 'data' (case-sensitive)
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Bar Chart'},
                    {'x': [1, 2, 3], 'y': [2, 4, 1], 'type': 'line', 'name': 'Line Chart'}
                ],
                'layout': {
                    'title': 'GRAPH TITLE',
                    'xaxis': {'title': 'X-AXIS TITLE'},
                    'yaxis': {'title': 'Y-AXIS TITLE'}
                }
            }
        )
    ]
)

# RUNNING THE DASH APPLICATION
if __name__ == '__main__':
    app.run(debug=True)
