### Assignment Chapter 9 - Creating Class
## 9-4
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

# Create Instance
mirpur = Restaurant("Rabbani","Chicken-kabab")               
print(f"My favourite restaurant in Mirpur is {mirpur.restaurant_name}.")
#Calling method
mirpur.describe_restaurant()
print(f"The restaurent serverd {mirpur.number_served} customers at the fisrt day.")
# mirpur.number_served = 200
# print(f"Now {mirpur.restaurant_name} servers {mirpur.number_served} customers daily.")
mirpur.set_number_served(200)
print(f"Now {mirpur.restaurant_name} servers {mirpur.number_served} customers daily.")
mirpur.increment_odometer(300) 
mirpur.open_restaurant()