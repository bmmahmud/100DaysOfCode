## Assignment 10 - 6
print("Enter two Number to add them.")
num1 = input("Number 1: ")
num2 = input("Number 2: ")
try:
    sum = int(num1) + int(num2)
except:
    print("WRONG INPUT TYPE!\nEnter of intege numbers.")
else:
    print(f"Addition of {num1} and {num2} is {sum}")