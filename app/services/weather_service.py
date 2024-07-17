import httpx

from app.fake_bd.bd import coordinates


async def get_weather_data(city: str):
    latitude, longitude = coordinates.get(city)

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

        # Пример обработки данных
        weather_data = [(time, temperature) for time, temperature in
                        zip(data["hourly"]["time"], data["hourly"]["temperature_2m"])]
        return weather_data
