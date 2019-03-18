#!/usr/bin/env python3

from flask import Blueprint,render_template,request, Flask, redirect, Response, request, g
import json

from src.model import model

controller = Blueprint('public',__name__)

controller.secret_key = "12344666689"

@controller.route('/')
def dashboard(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
	return render_template('index.html')

@controller.route('/graph1', methods=['GET', 'POST'])
def graph1():
    if request.method == 'GET':
        chart = {'type': 'column'}
        title = {'text': 'Monthly Average Rainfall'}
        subtitle = {'text': 'Source: WorldClimate.com'}
        xAxis = {'categories': ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],'crosshair': 'true'}
        yAxis = {'min': 0, 'title': {'text': 'Rainfall (mm)'}}
        plotOptions = {'column': {'pointPadding': 0.2, 'borderWidth': 0}}
        series = [{
                'name': 'Tokyo',
                'data': [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]

            }, {
                'name': 'New York',
                'data': [83.6, 78.8, 98.5, 93.4, 106.0, 84.5, 105.0, 104.3, 91.2, 83.5, 106.6, 92.3]

            }, {
                'name': 'London',
                'data': [48.9, 38.8, 39.3, 41.4, 47.0, 48.3, 59.0, 59.6, 52.4, 65.2, 59.3, 51.2]

            }, {
                'name': 'Berlin',
                'data': [42.4, 33.2, 34.5, 39.7, 52.6, 75.5, 57.4, 60.4, 47.6, 39.1, 46.8, 51.1]
            }]
        return render_template('graph1.html',series=series, chart=chart, title=title, subtitle=subtitle, xAxis=xAxis, yAxis=yAxis, plotOptions=plotOptions)

@controller.route('/graph2', methods=['GET', 'POST'])
def graph2():
    if request.method == 'GET':
        chart = {
            'plotBackgroundColor': 'null',
            'plotBorderWidth': 'null',
            'plotShadow': 'false',
            'type': 'pie'
        }
        title = {
            'text': 'Browser market shares in January, 2018'
        }
        plotOptions = {
            'pie': {
                'allowPointSelect': 'true',
                'cursor': 'pointer',
                'dataLabels': {
                    'enabled': 'true',
                    'format': '<b>{point.name}</b>: {point.percentage:.1f} %',
                    'style': {
                        'color': "(Highcharts.theme && Highcharts.theme.contrastTextColor) || 'white'"
                    }
                }
            }
        }
        series = [{
            'name': 'Brands',
            'colorByPoint': 'true',
            'data': [{
                'name': 'Chrome',
                'y': 61.41,
                'sliced': 'true',
                'selected': 'true'
                }, {
                'name': 'Internet Explorer',
                'y': 11.84
                }, {
                'name': 'Firefox',
                'y': 10.85
                }, {
                'name': 'Edge',
                'y': 4.67
                }, {
                'name': 'Safari',
                'y': 4.18
                }, {
                'name': 'Sogou Explorer',
                'y': 1.64
                }, {
                'name': 'Opera',
                'y': 1.6
                }, {
                'name': 'QQ',
                'y': 1.2
                }, {
                'name': 'Other',
                'y': 2.61
                }]
        }]
    return render_template('graph2.html',series=series, chart=chart, title=title, plotOptions=plotOptions)

@controller.route('/graph34', methods=['GET', 'POST'])
def get_graph34_index():
    if request.method == 'GET':
        return render_template('graph34.html')

@controller.route('/graphsearch')
def get_graph34():
    try:
        q = request.args["q"]
    except KeyError:
        return []
    else:
        if (q == "graph3"):
            data= model.graph3()
    return Response(json.dumps(data),mimetype="application/json")

    