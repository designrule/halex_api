# halex_api


# インストール

```
$ pip install halex_api
```

# 使い方

```
from halex_api.api import Api

api = Api("HALEX AUTH_KEY")
api.get_weather_data("20191009", "20191010", 35.607285, 140.106495)
```

# 開発方法
```
$ docker-compose build
$ docker-compose up -d
```
