import requests
import json
import utilities as utl
import matplotlib.pyplot as plt
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html

# user name
name = 'Targgus'

# assign base info to variable
baseInfo = utl.getBaseInfo(name)

# init baseInfo class
baseInfoClass = utl.baseInfo(
    baseInfo['name'],
    baseInfo['level_pve'],
    baseInfo['pid']
)


# print(baseInfoClass.name)

# assign advanced info to variable using pid
advInfo = utl.getAdvancedStats(baseInfoClass.pid)

# build kill class
killsClass = utl.kills(
    advInfo['kills_total'],
    advInfo['kills_bleeding'],
    advInfo['kills_shocked'],
    advInfo['kills_burning'],
    advInfo['kills_ensnare'],
    advInfo['kills_headshot'],
    advInfo['kills_skill'],
    advInfo['kills_turret']
)

# print(killsClass.killsTotal, killsClass.killsTurret)

print(killsClass.array())

array = killsClass.array()
xloc = np.arange(0, len(array), 1)
plt.figure(figsize=(10,15))
x = ['Total Kills', 'Bleeding Kills', 'Shocked Kills', 'Burning Kills', 
        'Ensare Kills', 'Headshot Kills', 'Skill Kills', 'Turret Kills']
plt.barh(x, array)
plt.xticks(rotation='vertical')
# plt.show()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


app.layout = html.Div(children=[
    html.H1(children='The Divison 2 Personal Stats',
    style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    
    dcc.Graph(
        id='bar-graph',
        figure={
            'data': [
                {'x': x, 'y': array, 'type': 'bar'}
            ],
            'layout': {
                'title': 'Division Stats'
            }
        }
    ),

    dcc.Graph(
        id='bar-graph2',
        figure={
            'data': [
                {'x': x, 'y': array, 'type': 'bar'}
            ],
            'layout': {
                'title': 'Division Stats'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)