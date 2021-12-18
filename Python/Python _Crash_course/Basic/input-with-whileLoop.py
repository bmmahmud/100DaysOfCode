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

### Assignment 7-1
carType = input('What kind of rental car you want?\n')
print('Let me see if I can find you '+carType)

## Assignemnt 7-2
passanger = int(input('How many cars you need?\n'))
if passanger > 5:
    print('Not avaible that much. only 4 cars is available.')
else:
    print('Avaible to rent.')