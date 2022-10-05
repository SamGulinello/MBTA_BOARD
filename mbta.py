import requests
from requests.auth import HTTPBasicAuth

API_KEY = "INSERT API KEY HERE"

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

def getStops(route):
    URL = baseURL + '/stops?filter[route]={}'.format(route)
    payload = requests.get(URL, headers=headers).json()

    return payload