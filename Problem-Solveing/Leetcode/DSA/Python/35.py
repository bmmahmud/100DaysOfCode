# # 35. Search Insert Position | 27/01/2022
# Problem Link: https://leetcode.com/problems/search-insert-position/
# Runtime: 44 ms, faster than 93.89% of Python3 online submissions for Search Insert Position.
# Memory Usage: 14.7 MB, less than 99.94% of Python3 online submissions for Search Insert Position.

def searching(nums,target):
    # main code started here
    high = len(nums) - 1
    low = 0
    while low <= high:
        mid = low +((high-low)//2)
        if nums[mid]  == target:
            return mid 
        elif nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
    return low    
    # ends here                
nums = [1,3,5,6]
target = 5
print(searching(nums,target))

