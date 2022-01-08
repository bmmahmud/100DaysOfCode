class Solution:
    def reverse(self, num: int) -> int:
        reversed_num = 0
        result = 0
        if num > 0:
            while num != 0:
                digit = num % 10
                reversed_num = reversed_num * 10 + digit
                num //= 10
            result = reversed_num     
        else:
            n = num*-1
            while n != 0:
                digit = n % 10
                reversed_num = reversed_num * 10 + digit
                n //= 10
            result = reversed_num*-1
        if not -2**31 < result <  2**31 -1:
            return 0
        return result
        
        