from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def weather_page():
    weather_data = get_weather_data("London")
    if weather_data:
        store_weather_data(weather_data)
        return render_template("weather.html", weather_data=weather_data)
    else:
        return "Error retrieving weather data"

if __name__ == "__main__":
    app.run(debug=True)