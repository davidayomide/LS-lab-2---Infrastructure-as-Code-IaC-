import pymongo

def store_weather_data(data):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["weather_db"]
    weather_data = db.weather_data
    weather_data.insert_one(data)