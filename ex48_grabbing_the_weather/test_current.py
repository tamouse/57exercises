import unittest
from unittest.mock import MagicMock, patch
import time
from ex48_grabbing_the_weather.current import *

import logging
logging.basicConfig(
    stream=sys.stderr,
    level=logging.DEBUG,
    format='%(asctime)-20s %(levelname)-10s %(message)s'
)

# Two ways to do the mocking out of the current time:
#
# The first, in test_too_soon_true, builds the mock explicitly,
# and passes it into the with patch statement.
#
# The second uses a decorator patch, and we explicitly set
# just the return value.
#
# I'm not sure which is better, if either. TMTOWTDS.

class TestCurrentWeather(unittest.TestCase):
    def setUp(self):
        self.cw = CurrentWeather()
        self.frozen_time = time.time()

    def test_too_soon_true(self):
        self.cw.cached_data = {
            'loc': {
                'retrieved_at': self.frozen_time
            }
        }
        mocktime = MagicMock(return_value = self.frozen_time)
        with patch('time.time', mocktime):
            self.assertTrue(self.cw.too_soon('loc'))

    @patch('time.time')
    def test_too_soon_false(self, mock_time_time):
        self.cw.cached_data = {
            'loc': {
                'retrieved_at': self.frozen_time
            }
        }
        mock_time_time.return_value = self.frozen_time + DEFAULT_INTERVAL + 1
        self.assertFalse(self.cw.too_soon('loc'))

    @patch('ex48_grabbing_the_weather.current.CurrentWeather.api_current_weather')
    def test_current_weather_first_time(self, mock_api_current_weather):
        mock_api_current_weather.return_value = {
            'retrieved_at': self.frozen_time
        }
        current_weather = self.cw.current_weather('loc','k')
        self.assertIn('lock', self.cw.cached_data)
        self.assertEqual(mock_api_current_weather.called, True)

    @patch('time.time')
    @patch('ex48_grabbing_the_weather.current.CurrentWeather.api_current_weather')
    def test_current_weather_second_time(self, mock_api_current_weather, mock_time_time):
        mock_api_current_weather.return_value = {
            'retrieved_at': self.frozen_time
        }
        mock_time_time.return_value = self.frozen_time
        self.cw.cached_data = {
            'lock': {
                'retrieved_at': self.frozen_time
            }
        }

        current_weather = self.cw.current_weather('loc','k')
        self.assertIn('lock', self.cw.cached_data)
        self.assertEqual(mock_api_current_weather.called, False)

    @patch('time.time')
    @patch('ex48_grabbing_the_weather.current.CurrentWeather.api_current_weather')
    def test_current_weather_second_time_after_interval(self, mock_api_current_weather, mock_time_time):
        mock_api_current_weather.return_value = {
            'retrieved_at': self.frozen_time + DEFAULT_INTERVAL + 1
        }
        mock_time_time.return_value = self.frozen_time + DEFAULT_INTERVAL + 1
        self.cw.cached_data = {
            'lock': {
                'retrieved_at': self.frozen_time
            }
        }

        # logging.debug("Cached data before test: {}".format(self.cw.cached_data))
        # logging.debug("Mocked time: {}".format(mock_time_time))
        current_weather = self.cw.current_weather('loc','k')
        # logging.debug("Cached data after test: {}".format(self.cw.cached_data))
        self.assertEqual(mock_api_current_weather.called, True)

    @patch('time.time')
    @patch('ex48_grabbing_the_weather.current.CurrentWeather.api_current_weather')
    def test_current_weather_with_different_units(self, mock_api_current_weather, mock_time_time):
        mock_api_current_weather.return_value = {
            'retrieved_at': self.frozen_time
        }
        mock_time_time.return_value = self.frozen_time
        self.cw.cached_data = {
            'locmetric': {
                'retrieved_at': self.frozen_time
            }
        }

        current_weather = self.cw.current_weather('loc','imperial')
        self.assertIn('locimperial', self.cw.cached_data)
        self.assertEqual(mock_api_current_weather.called, True)



if __name__ == '__main__':
    unittest.main()
