### Chapter 9: Section Inheritance | 19-01-2022


class Car():
    def __init__(self,make,model,year):
        """"Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """"Return a neatly formatted descriptive name."""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()
    def read_odometer(self):
        """"Print a statement showing the car's mileage."""
        print("This ca has "+ str(self.odometer_reading) + " miles on it.")
    def update_odometer(self,mileage):
        """"Set the odometer readig to the given value
        Rejec the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage    
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading += miles
    def fill_gas_tank(self):
        """"Over ride parent class by create same name function in childclass"""
        print("from Parent class!")    
class ElectronicCar(Car):
    """"Represent aspects of a car, specific to electronic vehicles."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.bettery_size = 70
    def describe_battery(self):
        """"Describe"""
        print("This car has a "+str(self.bettery_size)+ " -kWh battery.")        
    # Overriding Methods
    def fill_gas_tank(self):
        """"Over ride parent class by create same name function in childclass"""
        print("This car doesn't need a gas tank!")

# creating instance
my_tesla = ElectronicCar('tesla','model S',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()