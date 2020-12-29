# -*- coding: utf-8 -*-
# URI Online Judge | 1066
# Even, Odd, Positive and Negative
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