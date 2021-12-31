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
def build_person(first_name, last_name,age = ''):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person
         
