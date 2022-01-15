### Assignment Chapter 9 - Creating Class
## 9-1
class Restaurant():
    """" About any restaurant info """
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        """"Tell abour Name and items"""
        print(f"Most Famouse item of  {self.restaurant_name} is {self.cuisine_type}.")
    def open_restaurant(self):
        """"Tell that the restaurant is open."""
        print(f"{self.restaurant_name} is now Open !!!")
# Create Instance
mirpur = Restaurant("Rabbani","Chicken-kabab")               
print(f"My favourite restaurant in Mirpur is {mirpur.restaurant_name}.")
#Calling method
mirpur.describe_restaurant()
mirpur.open_restaurant()

print("#"*30)
## 9-2
uttora = Restaurant("Crush Station","Pizza")               
print(f"My favourite restaurant in Uttora is {uttora.restaurant_name}.")
#Calling method
uttora.describe_restaurant()
uttora.open_restaurant()