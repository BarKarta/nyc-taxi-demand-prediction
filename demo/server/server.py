import json
from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask import request

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
data = [{
        'name': "Chelsea",
        'values': [
            {'label': "Number of Drives", 'val': 100},
        ],
        'color': "#E31A1C",
        }]


def getWeather(date, time):
    # TODO MAKE FUNCTION
    return 1


def getTimeBinned(time):
    # TODO MAKE FUNCTION
    return 1


def getWeekDay(date):
    # TODO MAKE FUNCTION
    return 1


def getZoneName(zone):
    # TODO MAKE FUNCTION
    return 1


@ app.route('/books')
def index():
    return jsonify(data)


@app.route('/calc', methods=['POST'])
def get_input():
    zone = request.json['zone']
    date = request.json['date']
    time = request.json['time']
    # TODO Add the API and get the weather information needed, based on the data we are getting from the user
    temp_man, temp_min, hdd, cdd, precipitation, new_snow, snow_depth = getWeather(
        date, time)
    # TODO Convert the Time to a interval
    time_binned = getTimeBinned(time)
    # TODO Convert the Date to a WeekDay e.g 1/5/22 -> friday
    weekday = getWeekDay(date)
    # TODO Convert the Zone number to a zone name based on the map the user is look at ( The Map we use in the REACT part).
    zone_name = getZoneName(zone)
    return jsonify(f'Zone : {zone}, Data : {date}, Time : {time}')


if __name__ == '__main__':
    app.run(debug=True)
