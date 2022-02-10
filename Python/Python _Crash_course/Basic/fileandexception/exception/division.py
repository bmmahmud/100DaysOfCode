## Exception Handel zero divisionError
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

## More details
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    frist_number = input("\nFirst number: ")
    if frist_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(frist_number) / int(second_number)
    except ZeroDivisionError:
        print("You can not divide by zero!")    
    else:
        print(answer)