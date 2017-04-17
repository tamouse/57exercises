
import os
import configparser
import datetime
import json
import logging
import sys
import time
import urllib.request as request
import urllib.parse as parse

DEFAULT_INTERVAL = 10 * 60 # 10 minutes
DEFAULT_API_ENDPOINT = 'http://api.openweathermap.org/data/2.5/weather'


class CurrentWeather:
    def __init__(self,
                 app_id=None,
                 interval=DEFAULT_INTERVAL,
                 endpoint=DEFAULT_API_ENDPOINT
    ):
        if app_id == None:
            self.app_id = self.get_app_id()
        else:
            self.app_id = app_id
        self.interval = interval
        self.endpoint = endpoint
        # TODO: turn this into a memoizing function
        self.cached_data = {}

    def current_weather(self, location, units):
        """
        This is the primary method of the class, it returns the current weather,
        possibly using a cached value if the method has been called recently
        for the given location.

        @param location [String] - the location to retrieve data from, this is the
        zip code and the country code as a sting: '99999,cc', e.g. '94040,us' is
        Mountian View, California, USA

        @param units [String] - one of 'imperial', 'metric', 'kelvin'

        @returns weather data [dict]
        """
        key = str(location)+str(units)
        if not self.too_soon(key):
            self.cached_data[key] = self.api_current_weather(location, units)
        return self.cached_data[key]

    def get_app_id(self):
        # This let's me keep the app ID I got from the openweathermap service
        # private; THe config file is kept in my home directory, under tighter
        # control (the file is user read-write only) and never becomes part of
        # the repository.
        config_file = os.path.join(os.environ.get('HOME'),'.config','openweathermap.org.ini')
        config = configparser.ConfigParser()
        config.read(config_file)
        return config['current']['appid']

    def too_soon(self, key):
        last_time = self.cached_data.get(key,{}).get('retrieved_at', 0)
        current_time = time.time()
        # logging.debug("Current time: {}".format(current_time))
        return (current_time - last_time) < self.interval

    def api_current_weather(self, location, units):
        """
        Direct call to the weather api.

        @params location [String] - zip location '99999,us'
        @params units [String] - 'imperial', 'metric', 'kelvin'
        """
        query = {
            'zip': location,
            'appid': self.app_id,
            'units': units
        }
        params = parse.urlencode(query)
        url = "{}?{}".format(self.endpoint, params)
        logging.debug("Url: {}".format(url))
        response = request.urlopen(url)
        if response.status == 200:
            data = json.loads(response.read().decode('utf-8'))
        else:
            data = {}

        data['retrieved_at'] = time.time()

        return data
