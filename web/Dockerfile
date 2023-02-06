FROM python:3.9-alpine

COPY web_server_service.py /app/

WORKDIR /app

RUN pip install flask

CMD ["python", "web_server_service.py"]
