from halex_api import __version__
from halex_api.api import Api


class TestApi:

    def setup_method(self):
        self.api = Api()

    def test_version(self):
        assert __version__ == '0.1.0'

    def test_halex_get(self):
        result = self.api.get_weather_data("20191009", "20191010", 35.607285, 140.106495)
        assert "Data" in result
