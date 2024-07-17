from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from starlette.templating import Jinja2Templates

from app.services.weather_service import get_weather_data
from app.fake_bd.bd import coordinates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.post("/weather", response_class=HTMLResponse)
async def get_weather(request: Request):
    form = await request.form()
    city = form.get("city")
    if city not in coordinates:
        return templates.TemplateResponse(request, name="error.html", context={"request": request, "error_message": 'Мне очень жаль, но мы не смогли найти такой город. Попробуйте еще раз.'})
    weather_data = await get_weather_data(city)
    return templates.TemplateResponse(request, name="result.html", context={"request": request, "weather": weather_data, "city": city})

@router.get("/cities", response_class=JSONResponse)
async def get_cities():
    return list(coordinates.keys())
