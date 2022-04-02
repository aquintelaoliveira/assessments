import utils
from fastapi import FastAPI
import uvicorn
from controller import index_controller, openweathermap_controller

app = FastAPI()

# add routes
app.include_router(index_controller.router)
app.include_router(openweathermap_controller.router)

if __name__ == "__main__":
    config = utils.getConfig()
    uvicorn.run(app, host=config['server']['host'], port=config["server"]['port'])