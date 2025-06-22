from flask import Flask
from gps_wrapper import GpsWrapper as GpsService

gps = GpsService("PA1010D")

app = Flask(__name__)

@app.route("/")
def home():
    return gps.getlocation().get()