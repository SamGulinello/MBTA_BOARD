import time
from datetime import datetime
from flask import Flask, render_template
from collections import OrderedDict

import mbta
import stops

API_KEY = ""

if(API_KEY):
    mbta.API_KEY = API_KEY
else:
    mbta.API_KEY = input("MBTA API Key -> ")

# Target Station
STATION_NAME = input("Target Station -> ")
MBTA_STATION = stops.MBTA_STOPS[STATION_NAME]

app = Flask(__name__)

class Train():
    def __init__(self, line, destination, arrivalTime, direction):
        self.line = line
        self.destination = destination
        self.arrivalTime = self.getRemainingTime(arrivalTime)
        self.direction = direction

    def getRemainingTime(self, arrivalTime):

        diff = arrivalTime - datetime.now()
        
        # API sometimes returns arrival times before current time
        if(datetime.now() < arrivalTime):
            return str((diff.seconds//60)%60) + " min"
        else:
            return None

def getPrintName(name):

    if name in stops.DESTINATION_STOPS:
        return stops.DESTINATION_STOPS[name]
    else:
        return name
    
@app.route('/getArrivals')
def getArrivals():
    predictions = mbta.getPredictions(MBTA_STATION)

    route = mbta.getRoute(predictions["data"][0]["relationships"]["route"]["data"]["id"])
    arrivals = []
    
    for p in predictions['data']:
        
        # Get Various IDs for search
        vehicleID = mbta.getVehicle(p["relationships"]["vehicle"]["data"]["id"])
        currentStopID = vehicleID['data']['relationships']['stop']['data']['id']  
        directionID = p['attributes']['direction_id']

        # Search with gathered IDs
        destination = route['data']['attributes']['direction_destinations'][directionID]
        arrivalTime = datetime.fromisoformat(p['attributes']['arrival_time']).strftime("%H:%M")
        currentStop = mbta.getStop(currentStopID)['data']['attributes']['name']

        if(len(arrivals) <= 6):
            arrivals.append({
                "arrivalTime" : arrivalTime,
                "destination" : destination,
                "currentStop" : currentStop
            })

        
    return arrivals

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()