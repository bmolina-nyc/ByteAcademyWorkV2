# Connecting Python to JavaScript 
- In this lesson we will learn how to pass variable from Python to JavaScript in order to visualize graphical data
- We will be using HighCharts as our visualization library 

### Getting Started
- Starting off, we assume that we have a Python Flask web setup which will pass variables to an HTML file
- We will learn how pass Python variables in two different manners: 1) will assume that we render a static page 2) we will enter a search entry in order to pull a graph 

### Static Graph
- Within in our HTML file we need the following code:
```HTML
<div id="container"></div>
```
- This will be the location where we render the graph
- In terms of JS, we need to import the scripts need for HighCharts
```HTML
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
    <script src="https://code.highcharts.com/highcharts.js"></script>
    <script src="https://code.highcharts.com/modules/exporting.js"></script>
    <script src="https://code.highcharts.com/modules/export-data.js"></script>
```
- And we also need the code for rendering the High Chart 
- The following code will be used underneath in the script import statements
```HTML
    <script>
        const series = ({{series|safe}})
        const chart = ({{chart|safe}})
        const title = ({{title|safe}})
        const subtitle = ({{subtitle|safe}})
        const xAxis = ({{xAxis|safe}})
        const yAxis = ({{yAxis|safe}})
        const plotOptions = ({{plotOptions|safe}})
        Highcharts.chart('container', {
        chart: chart,
        title: title,
        subtitle: subtitle,
        xAxis: xAxis,
        yAxis: yAxis,
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: plotOptions,
        series:series
        });
    </script>
```
- `const series = ({{series|safe}})` is the Jinja syntax we need to use in order to 'safely' pass the variable to JS 
- If we take a look at the Python public.py file, we can see the variables passed along with render_template 
```python
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
```

### Querying a Graph
- Querying the data for a specific chart is a little more difficult as we will need to match route paths on both the JS side and the Flask side
- Let's first start by setting up the HTML file with an input form and also add the necessary libraries 
- This is where will we input which graph we'd like to search for 
```HTML
    <form role = "search" id = "graphsearch">
        </div>
            <input type = "text" class="form-control" placeholder="graph3 or graph4" type="text" name = "graphsearch">
        </div>
    </form>
    <div id="container"></div>
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
        <script src="https://code.highcharts.com/highcharts.js"></script>
        <script src="https://code.highcharts.com/modules/exporting.js"></script>
        <script src="https://code.highcharts.com/modules/export-data.js"></script>
```
- Underneath the import scripts, we will add the JS code and examine each of the critical components. The following will be in between two more `<script>` tags
```js
    $(function () {
        function search() {
            let query=$("#graphsearch").find("input[name=graphsearch]").val();
            $.get("/graphsearch?q=" + encodeURIComponent(query),            
                    function (query) {
                        const chart = query['chart']
                        const title = query['title']
                        const subtitle = query['subtitle']
                        const tooltip = query['tooltip']
                        const plotOptions = query['plotOptions']
                        const series = query['series']
                        const xAxis = {
                            allowDecimals: false,
                            labels: {
                                formatter: function () {
                                    return this.value;
                                }
                            }
                        }
                        const yAxis = {
                            title: {
                                text: 'Nuclear weapon states'
                            },
                            labels: {
                                formatter: function () {
                                    return this.value / 1000 + 'k';
                                }
                            }
                        }
                        Highcharts.chart('container', {
                            chart: chart,
                            title: title,
                            subtitle: subtitle,
                            xAxis: xAxis,
                            yAxis: yAxis,
                            tooltip: tooltip,
                            plotOptions: plotOptions,
                            series:series
                            });
                        if (!query) return;
                    }, "json");
            return false;
        }
        $("#graphsearch").submit(search);
        search();
    })
```
- `let query=$("#graphsearch").find("input[name=graphsearch]").val();` allows us to search the HTML for for the `<div>` tag with the name `graphsearch` whenever the `graphsearch` path is rendered from Flask
- `$.get("/graphsearch?q=" + encodeURIComponent(query),` then routes us to the path `/graphsearch?q=` + the specific search parameter we typed in. `query` would be our search input 
- Finally, below is how we call on the search function whenever the page is rendered
```javascript
    $("#graphsearch").submit(search);
    search();
```
- Now on the Python side we need to create 3 different methods. 
- The first two are for routes in your public.py file and the other will be a method in your model.py file 
- The first route we create will direct us to our graph34 page in and the 2nd route will allow us to run a search within the graph34 HTML file 
```python
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
```
- In this example, `q = request.args["q"]` is how we get and pass the query from JS. As you may recall, we used `$.get("/graphsearch?q=" + encodeURIComponent(query),` in order to get the search parameter
- Now we set the condition for a given search paramenter and then pass the data
- In my `model.py` I parse my data separately so that it does not crowd up the file 
```python
def graph3():
    chart = {
        'type': 'area'
    }

    title={
        'text': 'US and USSR nuclear stockpiles'
    }

    subtitle={
        'text': 'Sources: <a href="https://thebulletin.org/2006/july/global-nuclear-stockpiles-1945-2006">' +
        'thebulletin.org</a> &amp; <a href="https://www.armscontrol.org/factsheets/Nuclearweaponswhohaswhat">' +
        'armscontrol.org</a>'
    }

    tooltip = {
        'pointFormat': '{series.name} had stockpiled <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    }

    plotOptions = {
        'area': {
            'pointStart': 1940,
            'marker': {
                'enabled': 'false',
                'symbol': 'circle',
                'radius': 2,
                'states': {
                    'hover': {
                        'enabled': 'true'
                    }
                }
            }
        }
    }
    series = [{
        'name': 'USA',
        'data': [
        0, 0, 0, 0, 0, 6, 11, 32, 110, 235,
        369, 640, 1005, 1436, 2063, 3057, 4618, 6444, 9822, 15468,
        20434, 24126, 27387, 29459, 31056, 31982, 32040, 31233, 29224, 27342,
        26662, 26956, 27912, 28999, 28965, 27826, 25579, 25722, 24826, 24605,
        24304, 23464, 23708, 24099, 24357, 24237, 24401, 24344, 23586, 22380,
        21004, 17287, 14747, 13076, 12555, 12144, 11009, 10950, 10871, 10824,
        10577, 10527, 10475, 10421, 10358, 10295, 10104, 9914, 9620, 9326,
        5113, 5113, 4954, 4804, 4761, 4717, 4368, 4018
        ]
    }, {
        'name': 'USSR/Russia',
        'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        5, 25, 50, 120, 150, 200, 426, 660, 869, 1060,
        1605, 2471, 3322, 4238, 5221, 6129, 7089, 8339, 9399, 10538,
        11643, 13092, 14478, 15915, 17385, 19055, 21205, 23044, 25393, 27935,
        30062, 32049, 33952, 35804, 37431, 39197, 45000, 43000, 41000, 39000,
        37000, 35000, 33000, 31000, 29000, 27000, 25000, 24000, 23000, 22000,
        21000, 20000, 19000, 18000, 18000, 17000, 16000, 15537, 14162, 12787,
        12600, 11400, 5500, 4512, 4502, 4502, 4500, 4500
        ]
    }]

    data = {
        'chart' : chart,
        'title' : title,
        'subtitle' : subtitle,
        'tooltip': tooltip,
        'plotOptions': plotOptions,
        'series': series
    }
    return (data)
```
- Finally, I return a `Response` in JSON format because that is currently the format I have set in HTML 

CONGRATULATIONS! You have successfully connected python to javascript!
