from flask import Flask
from gps_wrapper import LocationData, GpsWrapper as GpsService
from pa1010d import PA1010D
import json

gps = GpsService("PA1010D")

app = Flask(__name__)

@app.route("/")
def home():
    return gps.getlocation().get()

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
