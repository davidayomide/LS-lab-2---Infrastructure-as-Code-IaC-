FROM python:3.9-alpine

COPY data_storage_service.py /app/

WORKDIR /app

RUN pip install pymongo

CMD ["python", "data_storage_service.py"]
