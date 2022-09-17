import urllib.request
from openWeather_website import*
import json

# Defining the function for generating weather report of location according to user wish .
# we used visualcross_website for web scraping
def reportFormate3():
    try:
        location = input("Enter Location: ")
        url = (f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/' +location + '?unitGroup=us&key=57CTJGT8P2QKLMLZRR7AGP7S6&contentType=json')
        req = urllib.request.urlopen(url).read().decode()#passing a dictionary parameter to urllib.urlopen
        data = json.loads(req)
        address= data["resolvedAddress"]
        tempmax = data['days'][0]["tempmax"]
        tempmin = data['days'][0]["tempmin"]
        description = data['days'][0]['description']
        weather.add_run("\n---------Visual Cross.com---------\n ").bold = True
        weather.add_run(f"Location:{address}\nMaximum Temperature :{tempmax}\nMinimum temperature :{tempmin}\ndescription:{description}").arial=True
        weather.add_run("\n----------------------------------------------------------------------------------\n")
    except:
        print("oops .... location not found  ")



