#!/usr/bin/env python
import urllib2
import json
from flask import Flask, render_template
import pdb
import platform

app = Flask(__name__)


@app.route('/')
def helloweather():
    # Return my IP and lon/lat
    req = urllib2.Request('http://ipinfo.io')
    req.add_header('User-Agent', 'curl')
    response = urllib2.urlopen(req)
    geoip_params = ''
    try:
        geoip_params = json.loads(response.read())
    except:
        print "Couldn't retrieve your IP / location"

    lat, lon = geoip_params['loc'].split(',')
    print lon, lat
    weatherurl = "http://forecast.weather.gov/MapClick.php?lat=%s&lon=%s&FcstType=json" % (lat, lon)
    weatherdata = urllib2.urlopen(weatherurl)
    dictweatherdata = ''
    try:
        dictweatherdata = json.loads(weatherdata.read())
    except:
        print "Couldn't retrieve weather in your area :("
    return render_template('hello.html', weatherdata=dictweatherdata, hostname=platform.node())

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5555)
