import utils
import requests
from model import openweathermap_model
from fastapi import HTTPException

__url = "http://api.openweathermap.org/data/2.5/weather"
__params = {
    'appid': utils.getConfig()['api_key']['openweathermap'],
    'units': "metric"
}

def getWeatherByCityId(id: int):
    __params['id'] = id
    response = requests.get(url=__url, params=__params)
    json_response = response.json()

    if(response.status_code != 200):
        raise HTTPException(
            status_code=response.status_code,
            detail=json_response['message']
        )

    return json_response

def getWeatherByCityName(name: str):
    __params['q'] = name
    response = requests.get(url=__url, params=__params)
    json_response = response.json()

    if(response.status_code != 200):
        raise HTTPException(
            status_code=response.status_code,
            detail=json_response['message']
        )

    return weather_mapper(json_response)

def weather_mapper(json_response: object):
    return openweathermap_model.Weather(
        name = json_response['name'],
        temp = json_response['main']['temp'],
        description = json_response['weather'][0]['description']
    )
