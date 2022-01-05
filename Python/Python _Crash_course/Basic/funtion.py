### Python Crush Course - 29 Dec 2021 | Funtion - Chapter 8
## simple function 
# def greet_user():
#     """"Display a simple greeting.""" #docstring
#     print("Hello")
#greet_user() ## call function

## passing information
# def greet_user(username):
#     """"Display username with greeting."""
#     print("Hello, "+ username.title() + "!")

# greet_user("Ashik")

### Assignment 8-1
# def display_message():
#     print("I learn Complete python from this book.")
# display_message()    

# def favorite_book(book_name):
#     print("My favorite books is "+book_name+"!")
# favorite_book('Alice in Wonderland')    

### Multi arguments
# def describe_pet(animal_type, pet_name):
#     """"Display information about a pet."""
#     print("\nI have a "+animal_type +".")
#     print("My "+animal_type+"'s name is "+ pet_name.title() +'.')
# describe_pet('hamster','harry')

### define key word
# def describe_pet(animal_type, pet_name):
#     """"Display info"""
#     print("\nI have a "+animal_type +".")
#     print("My "+animal_type + "'s name is "+ pet_name.title()+".")
# describe_pet(animal_type='hamster',pet_name='harry')


### Assignment 8-3
# def make_shirt(size,text="I love Python"):
#     print("The Shirt Size is "+size+".")
#     print("Shirt Text on it "+text)
# make_shirt(size='M')

#### Return Value
# def get_formatted_name(first_name, last_name):
#     """"Return a full name, neatly formatted."""
#     full_name = first_name + " " + last_name
#     return full_name.title()
# person_name = get_formatted_name('ashik','mahmud')
# print(person_name)  


### optional argument
# def get_formatted_name(first_name,last_name,middle_name=''):
#     if middle_name:
#         full_name = first_name.upper() + " " + middle_name.title() + " " + last_name.title()
#     else:
#         full_name = first_name.upper() + " " + last_name.title()  
#     return full_name
# person = get_formatted_name('bm','mahmud','ashik')    
# print(person)          

### Dictionary return
# def build_person(first_name, last_name,age = ''):
#     person = {'first':first_name,'last':last_name}
#     if age:
#         person['age'] = age
#     return person
# musician = build_person('jimi','mahmd',age=26)
# print(musician)    

### Function with while loop
# def get_formatted_name(first_name, last_name):
#     """"Return a full name, neatly formatted."""
#     full_name = first_name + " " + last_name
#     return full_name.title()
# # This is an infinite loop!

# while True:
#     print("\n Please tell me your name:")
#     print("(Enter 'q' at any time to quit)")
#     f_name = input("First Name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last Name: ")
#     if l_name == 'q':
#         break
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, "+ formatted_name + "!")

#### Assignment 8-6
# def city_country(fname,lname):
#     full_name = fname +", "+lname
#     return full_name.title()

# name = city_country('samtiago','chile')  
# print(name)  



### Passign List in funtion
# def greet_users(users):
#     for name in users:
#         msg = "Hello, " + name.title() + "!"
#         print(msg)
# username = ['ashik','abir','lamia']
# greet_users(username)  



# #### Modifying a list
## move completed design
# def printed_model(unprinted_designs,completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print("Printing model: "+ current_design)
#         completed_models.append(current_design) # store in a new list
# def show_completed_models(completed_models):
#     print("\nThe following models havve been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
# #declareing list 
# unprinted_designs = ['iphone case','robot pendant','dodecahedron']
# completed_models = []  

# #call function
# printed_model(unprinted_designs[:],completed_models) # paasing a copy of the list by slice
# show_completed_models(completed_models)

### Assignment 8-9, 8-10
# def make_great(names):
#     for i in range(len(names)):
#         names[i] = "Great "+names[i]
    
# def show_magicians(names):
#     for name in names:
#         print(name.title())

# magicians_name = ['ashik','abir','lamia']
# make_great(magicians_name)
# show_magicians(magicians_name)

### Passing an arbitrary number of arguments
# def make_pizza(size,*toppings):
#     # print("\nMaking a pizza with the following toppings:")
#     print("\nMaking a " + str(size)+ "-inch pizza with the following toppings:") 
#     for topping in toppings:
#         print("- "+ topping)
# make_pizza(3,'pepperoni')
# make_pizza(6,'mashrooms','green peppers','extra cheese')

### Dictionary as argument
# def build_profile(first, last,**user_info):
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value   
#     return profile
# user_profile = build_profile('albert','einstein',locals='princeton',field='physics',age='24') 
# print(user_profile)            

### Assignment 8-12
# def make_sandwiches(*items):
#     print("\nFolloing items are begin added to Sandwiches:")
#     for item in items:
#         print("- "+item.title())
# make_sandwiches('tomato')
# make_sandwiches('fish','meat','salad')

#### Assignment 8-13 
# def build_profile(first, last,**user_info):
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value   
#     return profile
# user_profile = build_profile('ashik','mahmud',locals='mirpur',field='CSE',age='27') 
# # print(user_profile) 
# profile = ['First Name','Last Name','Home Location','Bachelor Field','Age']
# for key, value in user_profile.items():
#         for title in profile:
#             print(title+": "+value)

### Work with another file by import
# import pizza
# make_pizza(16,'pepperoni')
# pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')

# calling specific function from a module
from pizza import make_pizza 
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

### Using as to Give a Function an Alias
from pizza import make_pizza as mp

mp(16,'pepperoni')
mp(12,'mushrooms','green peppers','extra cheese')

### Call all function
# from pizza import * 