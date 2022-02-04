# https://leetcode.com/problems/guess-number-higher-or-lower/
# 374. Guess Number Higher or Lower

### My solution
# class Solution:
#     def guessNumber(self, n: int) -> int:
#         l=1
#         h=n
#         while l<=h:
#             m = (h+l)//2
#             if guess(m) == 0:
#                 return m
#             elif guess(m) > 0:
#                 l = m +1
#             else:
#                 h = m - 1
#         return m    

### Best Solution
# class Solution:
#     def guessNumber(self, n: int) -> int:
#         l, h = 1, n
#         while l < h:
#             mid = (l+h)//2
#             if guess(mid) == 1:
#                 l = mid+1
#             else:
#                 h = mid
#         return l