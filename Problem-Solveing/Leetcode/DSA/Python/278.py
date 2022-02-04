# # 278. First Bad Version | 27/01/2022
# Problem Link: https://leetcode.com/problems/first-bad-version/

### My Solution
## Runtime: 31 ms, faster than 67.75% of Python3 online submissions for First Bad Version.
## Memory Usage: 13.9 MB, less than 98.41% of Python3 online submissions for First Bad Version.
# class Solution:
#     def firstBadVersion(self, n: int) -> int:
        # l,h = 1,n
        # result = n
        # while l <= h:
        #     mid = (h+l)//2
        #     if isBadVersion(mid):
        #         result = mid
        #         h = mid -1
        #     else:
        #         l = mid + 1
        # return result  

#### best Soluton
# class Solution:
#     def firstBadVersion(self, n: int) -> int:
     
#         left = 0
#         right = n
#         while left < right:
#             mid = (left + right) // 2
#             res = isBadVersion(mid)
#             if res == True:
#                 right = mid
#             else:
#                 left = mid + 1
#         return right
        
### other Soltion Collected
# class Solution:
#     def firstBadVersion(self, n: int) -> int:
        
#         left, right = 1, n
#         while left <= right:
#             midpoint = math.floor((left+right)/2)
#             if isBadVersion(midpoint) == False:
#                 if isBadVersion(midpoint+1) == True:
#                     return midpoint + 1
#                 left = midpoint
#             else:
#                 if isBadVersion(midpoint-1) == False:
#                     return midpoint
#                 else:
#                     right = midpoint