# leedCode : 9 Palindrome Number [05/12/2021]

number = -121

reverse = 0
while(number >0):
    reminder = number % 10
    reverse = reverse * 10 + reminder
    number = number // 10
if number == reverse:
    print("\nReverse Number: {0}".format(reverse))
else:
    print("Not Same")   
print("\nReverse Number: {0}".format(reverse))         

