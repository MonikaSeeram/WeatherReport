import requests
# Defining the function for generating weather report of location according to user wish .
#Here we used wttr url to web scrap
def reportFormate4():
    try:
        location = input('Enter location: ')
        url = 'https://wttr.in/{}'.format(location)
        res = requests.get(url)
        print(res.text)#directly prints the output which was predesigned by that website
    except:
        print("oops .... location not found  ")





