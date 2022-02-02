class Restaurant():
    """" About any restaurant info """
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  
    def describe_restaurant(self):
        """"Tell abour Name and items"""
        print(f"Most Famouse item of  {self.restaurant_name} is {self.cuisine_type}.")
    def open_restaurant(self):
        """"Tell that the restaurant is open."""
        print(f"{self.restaurant_name} is now Open !!!")
    def set_number_served(self,number):
        self.number_served = number
    def increment_odometer(self,customer):
        self.number_served += customer
        if customer > 200:
            print("A great Business Day")
class IceCreamStand(Restaurant):
    """"Represent aspects of a car, specific to electronic vehicles."""
    def __init__(self, name, cuisine_type='ice cream'):
        """Initialize an ice cream stand."""
        super().__init__(name, cuisine_type)
        self.flavors = []
    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())