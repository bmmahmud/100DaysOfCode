# If condition
cars = ['audi','bmw','subaru','toyota']

# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title()) 

### Check value in list 
# car = 'bmw'
# if car in cars:
#     print(car.upper())    

# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')

# print("\nIs car == 'audi'? I predict Flase.")
# print(car == 'audi')

# for car in cars:
#     if car == 'audi':
#         print(car == 'audi')
#     elif car == 'bmw':
#         print(car == 'bmw')
#     else:
#         print(car.title())   
         

# Muliple If else
# age = 25
# if age < 18:
#     print("You are Eligile to get married.")
# elif age < 30:
#     print('You are Mature Enough to get marrided.\nDo not be late.') 
# else:
#     print("Best of luck")  

# if 'bmw' in cars:
#     print('cars list have BMW')  

# # Assignment 5-3
# alien_color = ['green','yello','red']

# # if 'red' in alien_color:
# #     print("Player just earned 5 points!!")
# for color in alien_color:
#     print("Adding "+ color +"." )
# print("\nFinish Adding")    


## Multiple List - Pizza Topping
available_toppigs = ['mushrooms','olives','green pappers','pepperoni','pineapple','extra cheese']
requested_topping = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_topping:
    if requested_topping in available_toppigs:
        print("Adding "+ requested_topping+".")
    else:
        print("Sorry, We don't have "+requested_topping +".")
print("\nFinished making your pizza!")            
