from email import message


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

class Battery():
    """A simple attemp to model a battery for an electric Car."""
    def __init__(self,battery_size=70):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a Statement describing the battery Size."""
        print("This car has a "+ str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            self.range = 240
        elif self.battery_size == 85:
            self.range = 270
        message = "This car can go approximately " + str(self.range)
        message += " miles on a full charge."
        print(message)            

class ElectronicCar(Car):
    """"Represent aspects of a car, specific to electronic vehicles."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.bettery_size = 70
        self.battery = Battery()
    def describe_battery(self):
        """"Describe"""
        print("This car has a "+str(self.bettery_size)+ " -kWh battery.")        
   
