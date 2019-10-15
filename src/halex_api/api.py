import requests


class Api(object):
    def __init__(self, api_key):
        self.api_iey = api_key

    def get_weather_data(self, from_date, to_date, lat, lon):

        url = 'https://memory.halex.co.jp/wpast/hpd'
        # maxRange = 62
        params = {
            "sid": 'analysis-service',
            "lat": lat,
            "lon": lon,
            "rem": 'all',
            "gran": '5',
            "from": from_date,
            "to": to_date
        }

        headers = {
            "Authorization": self.api_iey
        }

        ret = requests.get(url, params=params, headers=headers)
        if (ret.status_code == 200):
            return ret.json()
        else:
            return {}
