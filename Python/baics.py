####### Swap
# x = int(input("1st Value:"))
# y = int(input("2nd Value:"))
# print("Values :",x,",",y)
# temp = x
# x = y
# y = temp
# print("Swap Values:",x,",",y)

##### Armstrong Number

num = int(input("Enter Number:"))
sum = 0 

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit **3 
    temp//= 10
if num == sum:
    print(num,"is an Armstrong number.")
else:
    print(num,"is not an Armstrong number.")         