# MBTA_BOARD

## About
This program is designed to run on a [Raspberry Pi](https//www.raspberrypi.com/) and 16 x 2 LCD display. It uses the [MBTA public API](https//www.mbta.com/developers/v3-api) to track the arrival times of the trains.

## Setup
To Use this code you will first need to generate an [API Key](https//api-v3.mbta.com/register). Insert the generated key in mbta.py. After that set up the Raspberry Pi and the LCD Display according to the schematic below.

![schematic](https://www.mbtechworks.com/wp-uploads/lcd1602-bb.jpg)

## Running
Finally after the device is set up just run main.py from the terminal. The program will prompt you for the station name of where you would like to target the arrivals. THIS STEP IS CASE SENSITIVE AND THE PROGRAM WILL CRASH IF DONE WRONG. Below is a list of all the stations in the MBTA. Once the station is in there might be a short delay as the Pi reaches out to the API. Once it gets data it will start to display it similar to how it is done on the Arrival boards at most T stops. It will cycle through both Inbound and Outbound destinations as well as all lines that are serviced at a given station.

- Government Center
- Park Street
- Boylston
- Arlington
- Copley
- Hynes Convention Center
- Kenmore
- Blandford Street
- Boston University East
- Boston University Central
- Amory Street
- Babcock Street
- Packard's Corner
- Harvard Avenue
- Griggs Street
- Allston Street
- Warren Street
- Washington Street
- Sutherland Road
- Chiswick Road
- Chestnut Hill Avenue
- South Street
- Boston College
- Cleveland Circle
- Englewood Avenue
- Dean Road
- Tappan Street
- Washington Square
- Fairbanks Street
- Brandon Hall
- Summit Avenue
- Coolidge Corner
- Saint Paul Street
- Kent Street
- Hawes Street
- Saint Mary's Street
- Riverside
- Woodland
- Waban
- Eliot
- Newton Highlands
- Newton Centre
- Chestnut Hill
- Reservoir
- Beaconsfield
- Brookline Hills
- Brookline Village
- Longwood
- Fenway
- Haymarket
- North Station
- Science Park/West End
- Lechmere
- Union Square
- Heath Street
- Back of the Hill
- Riverway
- Mission Park
- Fenwood Road
- Brigham Circle
- Longwood Medical Area
- Museum of Fine Arts
- Northeastern University
- Symphony
- Prudential
- Forest Hills
- Green Street
- Stony Brook
- Jackson Square
- Roxbury Crossing
- Ruggles
- Massachusetts Avenue
- Back Bay
- Tufts Medical Center
- Chinatown
- Downtown Crossing
- State
- Community College
- Sullivan Square
- Assembly
- Wellington
- Malden Center
- Oak Grove
- Alewife
- Davis
- Porter
- Harvard
- Central
- Kendall/MIT
- Charles/MGH
- South Station
- Broadway
- Andrew
- JFK/UMass
- Savin Hill
- Fields Corner
- Shawmut
- Ashmont
- North Quincy
- Wollaston
- Quincy Center
- Quincy Adams
- Braintree
- Bowdoin
- Aquarium
- Maverick
- Airport
- Wood Island
- Orient Heights
- Suffolk Downs
- Beachmont
- Revere Beach
- Wonderland

## Contributing
This is kind of a quick project for me so I won't be building it out much more. If you would like to contribute though please feel free to fork this repo and submit a pull request with the updates. I would love to see this take off.