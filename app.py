from flask import Flask, render_template
# , request, url_for
import plotly
import plotly.graph_objs as go
# import datetime
# from calendar import monthrange
import pandas as pd
import numpy as np
import json

from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

from collections import Counter
import plotly.express as px

app = Flask(__name__)
GoogleMaps(app)


@app.route('/charginga')
def index():
    plot1 = power_plot()
    plot2 = kwh_plot()
    plot3 = paytype_plot()
    plot4 = porttype_plot()
    evmap = Map(
        identifier="evmap",
        lat=21.300430,
        lng=-157.851510,
        style="height:350px;width:1535px;top:.5;left:0;position:absolute;z-index:200",
        markers=[
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 21.589029,
                'lng': -158.103653,
                'infobox': "<a href= https://www.tripadvisor.com/Attraction_Review-g60647-d10053296-Reviews-Haleiwa_Town_Center-Haleiwa_Oahu_Hawaii.html>Haleiwa Town Center</a>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 21.525810,
                'lng': -158.037781,
                'infobox': "<a href= https://www.tripadvisor.com/Attraction_Review-g60659-d105817-Reviews-Dole_Plantation-Wahiawa_Oahu_Hawaii.html>Dole Plantation</a>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 21.293831,
                'lng': -157.710403,
                'infobox': "<a href= https://7elevenhawaii.com/the-hawai%CA%BBi-kai-store/>Hawaii Kai 7-Eleven</a>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 21.436701,
                'lng': -157.826355,
                'infobox': "<a href= https://koolaucenter.com/>Koolau Center</a>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 21.300430,
                'lng': -157.851510,
                'infobox': "<a href= https://www.mapquest.com/us/hawaii/hawaiian-electric-company-350600396>Hawaiian Electric Ward Office</a>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 21.318001,
                'lng': -157.869293,
                'infobox': "<a href= https://www.costco.com/warehouse-locations/iwilei-honolulu-hi-687.html>Iwilei Costco Parking Lot</a>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 21.407749,
                'lng': -157.949615,
                'infobox': "<a href=http://images4.loopnet.com/d2/1RlDfIhhSvypMxZsElmlvjgW6W3a3WElYcyBzrLkhbc/document.pdf>Times Square Shopping Center</a>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 21.328870,
                'lng': -158.091470,
                'infobox': "<a href=https://kapoleicommons.com/>Kapolei Commons</a>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 21.436590,
                'lng': -158.184880,
                'infobox': "<a href= https://alexanderbaldwin.propertycapsule.com/properties/waianaemall/>Waianae Shopping Mall</a>"
            }]
    )
    return render_template('charginga.html', plot1=plot1, plot2=plot2, plot3=plot3, plot4=plot4, evmap=evmap, title='landing')


# @app.route('/charginga')
# def charginga():
#     feature = 'Bar'
#     bar = create_plot(feature)
#     bar2 = create_plot(feature)
#     
#     return render_template('charginga.html', plot=bar, plot2=bar2, plot3=plot1)


@app.route('/')
def landing():
    plot1 = power_plot()
    plot2 = kwh_plot()
    plot3 = paytype_plot()
    plot4 = porttype_plot()
    return render_template('index.html', plot1=plot1, plot2=plot2, plot3=plot3, plot4=plot4)


def create_plot(feature):
    if feature == 'Bar':
        N = 40
        x = np.linspace(0, 1, N)
        y = np.random.randn(N)
        df = pd.DataFrame({'x': x, 'y': y})  # creating a sample dataframe
        data = [
            go.Bar(
                x=df['x'],  # assign x as the dataframe column 'x'
                y=df['y']
            )
        ]
    else:
        N = 1000
        random_x = np.random.randn(N)
        random_y = np.random.randn(N)

        # Create a trace
        data = [go.Scatter(
            x=random_x,
            y=random_y,
            mode='markers'
        )]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


@app.route("/map")
def mapview():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 37.4419,
                'lng': -122.1419,
                'infobox': "<b>Hello World</b>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': 37.4300,
                'lng': -122.1400,
                'infobox': "<b>Hello World from other place</b>"
            }]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 37.4419,
                'lng': -122.1419,
                'infobox': "<b>Hello World</b>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': 37.4300,
                'lng': -122.1400,
                'infobox': "<b>Hello World from other place</b>"
            }]
    )
    evmap = Map(
        identifier="evmap",
        lat=21.300430,
        lng=-157.851510,
        markers=[
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 21.589029,
                'lng': -158.103653,
                'infobox': "<b>Haleiwa Town Center</b>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 21.525810,
                'lng': -158.037781,
                'infobox': "<b>Dole Plantation</b>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 21.293831,
                'lng': -157.710403,
                'infobox': "<b>Hawaii Kai 7-Eleven</b>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 21.436701,
                'lng': -157.826355,
                'infobox': "<b>Koolau Center</b>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 21.300430,
                'lng': -157.851510,
                'infobox': "<b>Hawaiian Electric Ward Office</b>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 21.318001,
                'lng': -157.869293,
                'infobox': "<b>Iwilei Costco Parking Lot</b>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 21.407749,
                'lng': -157.949615,
                'infobox': "<b>Times Square Shopping Center</b>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 21.328870,
                'lng': -158.091470,
                'infobox': "<b>Kapolei Commons</b>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 21.436590,
                'lng': -158.184880,
                'infobox': "<b>Waianae Shopping Mall</b>"
            }]
    )
    return render_template('map.html', mymap=mymap, sndmap=sndmap, evmap=evmap)


def power_plot():
    # DataA = pd.read_csv('Data_HACC.csv', nrows=6202)
    # DataB = pd.read_csv('Data_HACC.csv', skiprows=6202, nrows=10452)

    powerdata = pd.read_csv('Description-Table 1.csv', skiprows=6)
    power = powerdata['Power (kW)']
    # minkWh = powerdata['1-minute kWh']
    # totalkwh = powerdata['total kWh']
    timemin = [t for t in range(len(power))]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=timemin, y=power.tolist(), mode='lines', name='lines'))

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


def kwh_plot():
    powerdata = pd.read_csv('Description-Table 1.csv', skiprows=6)
    power = powerdata['Power (kW)']
    timemin = [t for t in range(len(power))]
    # minkWh = powerdata['1-minute kWh']
    totalkwh = powerdata['total kWh']
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=timemin, y=totalkwh.tolist(), mode='lines', name='lines'))
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


def paytype_plot():
    DataA = pd.read_csv('Data_HACC.csv', nrows=6202)
    # portlabels = ['CHADEMO','DCCOMBOTYP1']
    # paymentlabels = ['RFID','CREDITCARD']
    DataApaymentmode = DataA['Payment Mode'].values
    # DataApporttype = DataA['Port Type'].values

    # paysizes = [list(Counter(DataApaymentmode).values())[0],list(Counter(DataApaymentmode).values())[1]]
    # portsizes = [list(Counter(DataApporttype).values())[0],list(Counter(DataApporttype).values())[1]]

    colors = ['gold','skyblue']

    fig = go.Figure(data=[go.Pie(labels=['RFID','CREDITCARD'], values=[list(Counter(DataApaymentmode).values())[0],list(Counter(DataApaymentmode).values())[1]])])
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20, marker=dict(colors=colors, line=dict(color='#000000', width=2)))

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


def porttype_plot():
    DataA = pd.read_csv('Data_HACC.csv', nrows=6202)
    colors = ['gold','skyblue']
    DataApporttype = DataA['Port Type'].values
    
    fig = go.Figure(data=[go.Pie(labels=['RFID','CREDITCARD'], values=[list(Counter(DataApporttype).values())[0],list(Counter(DataApporttype).values())[1]])])
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20, marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON
if __name__ == '__main__':
    app.run(debug=True)
