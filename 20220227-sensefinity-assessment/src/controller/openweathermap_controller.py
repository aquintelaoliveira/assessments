import os
import json
from functools import wraps
from fastapi import APIRouter, status
from model import openweathermap_model
from service import openweathermap_service

def folder_weather_cache(func): 
    cache_dir = f"{os.getcwd()}\\src\\controller\\cache"
    @wraps(func)
    async def wrapper(*args, **kwargs):
        key = kwargs['id']
        if f"{key}.json" in os.listdir(cache_dir):
            print("cached")
            with open(f"{cache_dir}\\{key}.json") as f:
                result = json.load(f)
            return result
        else:
            result = func(*args, **kwargs)
            with open(f"{cache_dir}\\{key}.json", "w+") as f:
                json.dump(result, f)
            return result
    return wrapper

def weather_cache(func):
    cache = {} 
    @wraps(func)
    async def wrapper(*args, **kwargs):
        key = list(kwargs.values())[0]
        if key in cache:
            return cache[key]
        else:
            result = func(*args, **kwargs)
            cache[key] = result
            return result
    return wrapper

router = APIRouter(
    tags=["openweathermap"],
    prefix="/owm",
)

@router.get('/city/id/{id}', status_code=status.HTTP_200_OK)
@folder_weather_cache
def getWeatherByCityId(id: int):
    return openweathermap_service.getWeatherByCityId(id)

@router.get('/city/name/{name}', response_model=openweathermap_model.Weather, status_code=status.HTTP_200_OK)
@weather_cache
def getWeatherByCityName(name: str):
    return openweathermap_service.getWeatherByCityName(name)
