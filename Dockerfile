FROM python:2.7
EXPOSE 80
WORKDIR /app
ADD . /app
RUN touch index.html
CMD python index.py

