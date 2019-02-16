import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *

erfolgsfaktoren=pd.read_csv('/Users/stefanieloewer/PythonTraining/MeinErsterDashCode/erfolgsfaktoren.csv')

erfolgsfaktoren=erfolgsfaktoren.sort_values('Standardized Beta N1=310 Validation')



trace2 = go.Bar(
    y=erfolgsfaktoren['Success factors'],
    x=erfolgsfaktoren['Standardized Beta N1=310 Validation'],
    name='Validation N1=310',
    marker=dict(color='rgb(0, 154, 218)'),
    orientation = 'h'
)
trace1 = go.Bar(
    y=erfolgsfaktoren['Success factors'],
    x=erfolgsfaktoren['Standardized Beta N2=311 Other IT projects'],
    name='Other IT projects N2=311',
    marker=dict(color='rgb(192,192,192)'),
    orientation = 'h'
)

trace3 = go.Scatter(
    y=erfolgsfaktoren['Success factors'],
    x=erfolgsfaktoren['Standardized Beta N=639'],
    mode='lines+markers',
    line=dict(color='rgb(128, 0, 128)'),
    name='Success factors over all evaluated projects',
    orientation = 'h'
)

data = [trace1, trace2, trace3]

layout = go.Layout(
    title = 'Success factors of software development', # Graph title
    yaxis = dict(showticklabels=False,
                title = 'Success factors',
                 titlefont = dict(
                    family='Arial, sans-serif',
                    size=12,
                    color='rgb(0, 0, 0)'
            )),

    xaxis = dict(title = 'Standardized Beta coefficients',
                 titlefont = dict(
                    family='Arial, sans-serif',
                    size=12,
                    color='rgb(0, 0, 0)'
            ))
)

'''
annotations = []

y_alle = np.rint(erfolgsfaktoren['Standardized Beta N=639'])

# Adding labels
for yd, xd in zip(erfolgsfaktoren['Success factors'], erfolgsfaktoren['Standardized Beta N=639']):
    annotations.append(dict(xref='paper', yref='y',
                        x=0, y=yd,
                        xanchor='right',
                        text=str(yd),
                        font=dict(family='Arial', size=10, color='rgb(0, 0, 0)'),
                        showarrow=False, align='right'))

    annotations.append(dict(xref='paper', yref='paper',
                        x=-0.001, y=-0.2,
                        text='Stefanie Loewer  ' +
                             '"Erfolgsfaktoren softwaregestuetzter Validierungswerkzeuge"',
                        font=dict(family='Arial', size=10,
                                  color='rgb(150,150,150)'),
                        showarrow=False))

layout['annotations'] = annotations

'''

fig = go.Figure(data=data, layout=layout)

app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('SWsuccessfactor'),
    dcc.Graph(
        id='LoewerProject',
        figure=fig
    )])

if __name__ == '__main__':
    app.run_server(debug=True)
