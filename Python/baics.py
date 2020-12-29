####### Swap
# x = int(input("1st Value:"))
# y = int(input("2nd Value:"))
# print("Values :",x,",",y)
# temp = x
# x = y
# y = temp
# print("Swap Values:",x,",",y)

##### Armstrong Number

# num = int(input("Enter Number:"))
# sum = 0 

# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum += digit **3 
#     temp//= 10
# if num == sum:
#     print(num,"is an Armstrong number.")
# else:
#     print(num,"is not an Armstrong number.")         

even = 0 
odd=0
pos=0
neg=0
for x in range(5):
    num = int(input())
    if num%2 == 0:
        even+=1
    if num%2 == 1:
        odd+=1   
    if num>0:
        pos+=1
    if num<0:
        neg+=1    

print(even,"valor(es) par(es)")    
print(odd,"valor(es) impar(es)") 
print(pos,"valor(es) positivo(s)") 
print(neg,"valor(es) negativo(s)") 