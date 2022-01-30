# importing car call from another file 
from car import Car

# creating instance of Car class
my_new_car = Car('audi','a4',2016)

# Calling function of Car Class 
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 24
my_new_car.read_odometer()
