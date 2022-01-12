# # Declare Variables
# menue = { 1:{"item":"coffe","price":350},
# 2:{"item":"burgers","price":250},
# 3:{"item":"meatloaf","price":220},
# 4:{"item":"lasagna","price":220}
# }

# print(menue[1]['item'])

# # for item,value in menue.items():
# #         print(item,": Item: ",value["item"].title(),"- Price:"+str(value["price"])+"Tk") 

# Test 12/01/2022
# def numeric_validation(value):
#     while True:
#         try:
#             val = int(input(value))
#         except:
#             print('Please use numeric digits.')
#             continue
#         if val < 0:
#             print('Please enter a positive number.')
#             continue
#         else:
#             break
#     return val
# x = numeric_validation('Enter Item Name:')
# print(f'Your age is {x}.')

## if numeric then go
myVariable = input('Enter a number')
if myVariable in range(1,100):
    # Do something
    print(myVariable)
else:
    print('The variable is not a number')