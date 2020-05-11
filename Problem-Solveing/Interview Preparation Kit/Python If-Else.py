# https://www.hackerrank.com/challenges/py-if-else/problem
# Python If-Else
n = int(input())

if  n%2 != 0:
    print("Weird")
if n%2 == 0 and (n in range(2,6) or n > 20):
    print("Not Weird")
if n%2 == 0 and (n in range(6,21)):
    print("Weird")


    
    