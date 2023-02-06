FROM python:3.9-alpine

COPY weather_data_service.py /app/

WORKDIR /app

RUN pip install requests

CMD ["python", "weather_data_service.py"]
