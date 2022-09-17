import requests # To scrap the data
from openWeather_website import * # imports all from openweather website


api_key = "2e4bfb12170048639372b5c0470e6701"


# Defining the function for generating weather report of location according to user wish .
# we used weather bit website for web scraping
def reportFormate2():
    try:
        location = input('Enter location: ')
        print(".....................")
        api_key = "2e4bfb12170048639372b5c0470e6701"
        url_3 = 'https://api.weatherbit.io/v2.0/current?'
        full_url = url_3 + "&key=" + api_key + "&city=" + location
        res3 = requests.get(full_url)
        data3 = res3.json()
        temperature = (data3['data'][0]['temp'])
        wind_dir = (data3['data'][0]['wind_cdir_full'])
        description = (data3['data'][0]['weather']['description'])
        location = (data3['data'][0]['city_name'])
        weather.add_run("\n---------Weather Bit.com---------\n ").bold = True
        weather.add_run(
            f'Location : {location}\nTemperature: {temperature}\nWind Direction : {wind_dir}\nDescription:{description}').arial = True
        weather.add_run("\n----------------------------------------------------------------------------------\n")

    except:
        print("oops .... location not found ")





