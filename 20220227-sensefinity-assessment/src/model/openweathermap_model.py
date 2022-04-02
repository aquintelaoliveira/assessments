from pydantic import BaseModel

class Weather(BaseModel):
    name: str
    temp: str
    description: str
