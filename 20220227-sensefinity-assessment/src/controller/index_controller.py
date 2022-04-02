import utils
from fastapi import APIRouter, responses

__config = utils.getConfig()

router = APIRouter(
    tags=["index"],
)

@router.get("/")
def index():
    return responses.RedirectResponse(url=f"http://{__config['server']['host']}:{__config['server']['port']}/docs", status_code=303)
