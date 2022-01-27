# leedCode : 9 Palindrome Number [05/12/2021]

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         # return (str(x)[::-1] == str(x))
#         reverse = 0
#         if x < 0:
#             return False
#         reminder = x % 10
#         reverse = reverse * 10 + reminder
#         x = x//10
#         return reverse
x = 121
if x < 0:
    print("XFalse")
else:
    reverse = 0
    y = x
    while(x > 0):
        reminder = x % 10
        reverse = reverse * 10 + reminder
        x = x//10
    print(reverse)
    if reverse == x or x == reverse: 
        print("True",reverse,x)
    else:
        print('False',reverse,x)    

