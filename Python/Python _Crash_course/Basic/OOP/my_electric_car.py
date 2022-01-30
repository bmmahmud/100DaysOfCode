## calling Car class child Electric specifically
from car import ElectronicCar
## call multiple class
# from car import Car, ElectricCar

## Importing an Entire Module
#import car

## import all classes from a Module
# from module_name import *



my_tesla = ElectronicCar('tesla','model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()