# Input from user Chapter
# message = input("What is your name: ")
# print('Hello, '+message+'.Welcome to AI Survay.\nAnswer some questions:')
## Input int 
# age = int(input('How old are you?\n'))
# if age >= 18:
#     # print("You are alow to watch horror movies.")
# elif age < 0 :
#     print('try again')
# else:
#     print('You are not alow to watch horror movies.')

# ### Assignment 7-1
# carType = input('What kind of rental car you want?\n')
# print('Let me see if I can find you '+carType)

# ## Assignemnt 7-2
# passanger = int(input('How many cars you need?\n'))
# if passanger > 5:
#     print('Not avaible that much. only 4 cars is available.')
# else:
#     print('Avaible to rent.')


### While Loop
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

### Quit

# prompt = '\nTell me something, and I will repeat it back to you:'
# prompt += "\nEnter 'quit' to end the program."

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

### Assignment 7-4
# prompt = '\nTell me Topping for pizza:'
# prompt += "\nEnter 'quit' to end the program.\n"

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print("You will add "+message+" to your pizza!")


###     Assignment 7-5
# print("Know your ticket price according to Age-")
# message = ""
# while message != 'ok':
#     message = int(input("Tell me your age: "))
#     if message < 3:
#         print("Your Ticket is free.\n Type 'ok' to Exit")
#     elif message > 3 and message <= 12 :
#         print("Your ticket price is $10.\n Type 'ok' to Exit")
#     elif message > 12:
#         print("Your ticket price is $15.\n Type 'ok' to Exit")    


#### While Loop with Lists and Dictionaries
# unconfired_users = ['alive','brain','cabdace']
# confirmed_users = []

# while unconfired_users:
#     current_user = unconfired_users.pop()

#     print("Verifying user: "+ current_user.title())
#     confirmed_users.append(current_user)

#### Display all confirmed users.
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())    


#### Filling a Dictionary with User Input
# responses = {}

# polling_active = True

# while polling_active:
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")

#     responses[name] = response

#     repeat = input("Would you like to let another person respond? (yes/ no) ")
#     if repeat == 'no':
#         polling_active = False

# print("\n---- Poll Result ----")
# # print(responses)
# for name, response in responses.items():
#     print(name + " would like to climb " + response + ".")



# ###### Assignment 7-8
print(".....Order Management System....\n\n")
sandwitch_orders = []
order_list = True

while order_list:
    order = input("Enter your Sandwich order:")
    
    print("I am your "+order+" sandwitch.")
    sandwitch_orders.append(order)
    repeat = input("Would you like to order again? (yes/ no) ")
    if repeat == 'no':
        order_list = False

print(sandwitch_orders)
#------- Finish 
finished_sandwiches = []
while sandwitch_orders:
    move = sandwitch_orders.pop()
    # print("Verifying user: "+ move.title())
    finished_sandwiches.append(move)
# print(finished_sandwiches)

# finished_sandwiches = ['apple','banana','aa']
print("\nThe following Sandwiches are Finished:")
count = 1
# for confirmed_user in finished_sandwiches:
#     print(count+" "+confirmed_user.title()+" Sandwiches.")   
for num, name in enumerate(finished_sandwiches, start=1):
    # print(count+" "+confirmed_user.title()+" Sandwiches.")
    print("Order Number {}: {} Sandwiches is Finished".format(num, name))   