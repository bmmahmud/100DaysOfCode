# Functions
# big = 0
# for num in [2,4,6,7,3,1]:
#     if num > big:
#         big = num
#         print(big)
# print('Big:',big)

#### Functions
# def NameF(names):
#     print("Hello, "+names+". Good Morning")
# NameF("ashik")

####### Using Asterisks
# def NameF(*names):
#     for name in names:
#         print("Hello, "+name+". Good Morning") 
# NameF("ashik","lamia","abir")

####### Recursion
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))
# num = 6
# print("The Factorial of ",num," is ", factorial(num))            

# my_list = [1, 5, 4, 6, 8, 11, 3, 12]
# new_list = list(map(lambda x: x * 2 , my_list))
# print(new_list)

#### Global Variable
# x = "global"
# def foo():
#     print("x inside:",x)
# foo()
# print("x outside:",x)

## Gloabl Keyword
c = 0

def add():
    global c
    c = c+2
    print("Inside add():",c)

add()
print("In main:",c)    

