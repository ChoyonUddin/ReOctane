from datetime import datetime 
from tkinter import *
class Car:
    def __init__(self,brand:str,model:str,year:str,city_fuel_economy:float,highway_fuel_economy:float,combined_fuel_economy:float,kilometres_driven:float):
        self.brand = brand
        self.model = model
        self.year = year
        self.city_fuel_economy = city_fuel_economy
        self.highway_fuel_economy = highway_fuel_economy
        self.combined_fuel_economy = combined_fuel_economy
        self.kmd = kilometres_driven


#Next step is to implement tkinter such that the parameters for car are through user input
#After that some work with a slider for Kilometres_driven
#Then Frontend stuff
car = Car('Lexus','Nx 350h','2024',5.7,6.4,6,20000)

#Notes
'''
Variables for expense:
fuel economy: highway, city, combined
Price of the gas per day -> fluctates but used fixed price for now 
kilometres driven

#Later implementation
Add time later for day to day breakdown 
Car Fuel tank to show how much is left after each day and how many times a full refuel is required 
Price of gas per day web scraped from some website or an api
Select octane affects the price of gas
'''

formatted_date = datetime.now().strftime('%m/%d/%Y')

print(formatted_date)
print(car.kilometers_driven)