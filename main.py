import time
from datetime import datetime

import lcd
import mbta
import stops

# Target Station
STATION_NAME = input("Target Station -> ")
MBTA_STATION = stops.MBTA_STOPS[STATION_NAME]

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

def main():

    # Start LCD Output
    lcd.init()
    
    while(True):
        # get incoming train info
        predictions = mbta.getPredictions(MBTA_STATION)
        
        arrivals = []
        lines = set()
        for arrival in predictions["data"]:

            if(arrival["attributes"]["arrival_time"] != None):
                # Get destination info
                direction = arrival["attributes"]["direction_id"]
                line = arrival["relationships"]["route"]["data"]["id"]
                destination = mbta.getRoute(line)["data"]["attributes"]["direction_destinations"][direction]
                arrivalTime = datetime.strptime(arrival["attributes"]["arrival_time"][0:18], '%Y-%m-%dT%H:%M:%S')
                
                # Store data in object
                incoming = Train(line, destination, arrivalTime, direction)
                
                # Get rid of Green Line Branches
                lines.add(line[0:4])

                # Some bug was causing the target station to show as destination
                if(STATION_NAME not in destination and incoming.arrivalTime != None):
                    arrivals.append(incoming)

        # Loop Through Results By T Line
        for line in lines:
            # Break Up By Train Direction
            for direction in range(2):

                iteration = 0
                for train in arrivals:
                    if(line in train.line and train.direction == direction):

                        # Print Line 1
                        if(iteration == 0):
                            lcd.lcd_text("{}".format(getPrintName(train.destination) + " " + train.arrivalTime), lcd.LCD_LINE_1)
                            lcd.lcd_text("", lcd.LCD_LINE_2)
                        
                        # Print Line 2
                        elif(iteration == 1):
                            lcd.lcd_text("{}".format(getPrintName(train.destination) + " " + train.arrivalTime), lcd.LCD_LINE_2)

                            # Pause to display data
                            time.sleep(10)

                        # After two lines print the display can't show any more
                        else:
                            break
                        iteration += 1

if __name__ == "__main__":
    main()