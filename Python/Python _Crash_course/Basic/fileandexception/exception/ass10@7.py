## Assignment 10 - 7
print("Enter two Number to add them.")
while True:
    num1 = input("Number 1: ")
    if num1 == 'q':
        break
    num2 = input("Number 2: ")
    if num2 == 'q':
        break
    try:
        sum = int(num1) + int(num2)
    except:
            print("WRONG INPUT TYPE! Enter of intege numbers.")
    else:
        print(f"Addition of {num1} and {num2} is {sum}.\n type 'q' to exit")
              