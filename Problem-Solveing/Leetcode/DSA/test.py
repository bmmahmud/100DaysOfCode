nums = [1,3,5,6]
target = 3
high = len(nums) - 1
low = 0
while low <= high:
    mid = low +((high-low)//2)
    if nums[mid]  == target:
        print(mid) 
        break 
    elif nums[mid] > target:
        high = mid - 1
    elif nums[mid] < target:
        low = mid + 1
print(low)        