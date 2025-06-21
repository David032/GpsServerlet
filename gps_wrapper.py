from pa1010d import PA1010D

class LocationData():
    lattitude: float
    longitude: float

    def __init__(self, lat, long):
        global lattitude, longitude
        lattitude = lat
        longitude = long
    
    def get(self):
        return {"lat":lattitude, "long":longitude}
    
class GpsWrapper():
    gps = None
    mode:str

    def __init__(self, type:str):
        global gps, mode
        match type:
            case "PA1010D":
                gps = PA1010D()
            case "Adafruit":
                raise Exception("Adafruit support not yet implemented!")
            case _:
                raise Exception("Unrecognised module!")
        mode = type
            
    def update(self):
        match mode:
            case "PA1010D":
                gps.update()
            case "Adafruit":
                raise Exception("Adafruit support not yet implemented!")
            case _:
                raise Exception("Unrecognised module!")
    
    def getlocation(self):
        match mode:
            case "PA1010D":
                result = gps.update()
                if result:
                    return LocationData(gps.data["latitude"], gps.data["longitude"])
            case "Adafruit":
                raise Exception("Adafruit support not yet implemented!")
            case _:
                raise Exception("Unrecognised module!")
