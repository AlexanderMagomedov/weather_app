from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_weather_good_city():
    response = client.post("/weather", data={"city": "Moscow"})
    assert response.status_code == 200
    assert 'Moscow' in response.text


def test_weather_bad_sity():
    response = client.post("/weather", data={"city": "Makchachkala"})
    assert response.status_code == 200
    assert 'Мне очень жаль, но мы не смогли найти такой город. Попробуйте еще раз.' in response.text





