from openWeather_website import* # imports all from the generating_weatherReport module
from WeatherBit_website import*
from visualcross_website import *
from wttr_website import*
from output import display# importing display function from output module

#Iterating and calling the main function which was imported from generating_weatherReport module
choice = True
while (choice):
    reportFormate1()#calling the function from openWeather module .
    choice = input("Do you want to search for weather of another location [yes/no]:").lower()
    if choice == 'yes':
        reportFormate2()#calling the function from WeatherBit_website module
        choice = input("Do you want to search for weather of another location [yes/no]:").lower()
        if choice == 'yes':
            reportFormate3() # calling the visualcross_website module
            choice = input("Do you want to search for weather of another location [yes/no]:").lower()
            if choice == 'yes':
                reportFormate4()# calling the wttr_website module
                choice = input("Do you want to search for weather of another location [yes/no]:").lower()
            else:
                choice = False
        else:
            choice = False
    elif choice == 'no': # loop will break
        choice = False

display()# calling the function to display the report on word document
