# Weather App
Веб-приложение для получения прогноза погоды по введенному названию города.

## Использованные технологии

- FastAPI
- Open-Meteo API
- Docker
- Jinja2 для шаблонов
- httpx для асинхронных запросов
- pytest для тестов

## Запуск

1. Клонировать репозиторий
2. Установить зависимости:
    pip install -r requirements.txt
3. Запустить приложение:
    uvicorn app.main:app --reload
4. Запуск в Docker:
    docker build -t weather-app .
    docker run -p 8000:8000 weather-app
