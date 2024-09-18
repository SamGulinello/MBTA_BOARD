import requests
from requests.auth import HTTPBasicAuth

API_KEY = "30eae4835dfa48d5a7af510947a5fb81"

baseURL = 'https://api-v3.mbta.com'
headers = {'x-api-key': f'{API_KEY}'}

def getPredictions(station):
    URL = baseURL + '/predictions?filter[stop]={}'.format(station)
    payload = requests.get(URL, headers=headers).json()
    
    return payload

def getRoute(line):
    URL = baseURL + '/routes/{}'.format(line)
    payload = requests.get(URL, headers=headers).json()

    return payload

def getVehicle(line):
    URL = baseURL + '/vehicles/{}'.format(line)
    payload = requests.get(URL, headers=headers).json()

    return payload

def getStop(line):
    URL = baseURL + '/stops/{}'.format(line)
    payload = requests.get(URL, headers=headers).json()

    return payload

def getAlerts():
    URL = baseURL + '/alerts'
    payload = requests.get(URL,headers=headers).json()

    return payload

def getShapes(route):
    URL = baseURL + '/shapes?filter[route]={}'.format(route)
    payload = requests.get(URL, headers=headers).json()

    return payload

def getStops(route):
    URL = baseURL + '/stops?filter[route]={}'.format(route)
    payload = requests.get(URL, headers=headers).json()

    return payload