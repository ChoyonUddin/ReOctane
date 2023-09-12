import numpy as np
import timeit as t
from Main import car
#5.7/6.4/6.0
#problem with this is whilst it's readable and simple the entire "Main" file runs which is not ideal
def Expense(city: float, highway: float, combination_ting: float, ppl: float,kmd:int):
    annual_city = city * kmd//100 * ppl
    annual_highway = highway * kmd//100 * ppl
    annual_combined = combination_ting * kmd//100 * ppl
    print(annual_combined)
Expense(car.city_fuel_economy,car.highway_fuel_economy,car.combined_fuel_economy,1.50,car.kmd)

