# LeetCode: 34. Find First and Last Position of Element in Sorted Array | https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def search(self,nums, target,findStartIndex):
            # answer -1 if not found + start = fist index of list + End lenght of the list - 1
            ans,start,end = -1,0,(len(nums)-1)

            # check to find middle value as target value
            while start <= end:
                mid = ((start+(end-start)//2))  # middle value

                if target > nums[mid]:
                    start = mid + 1 
                elif target < nums[mid]:
                    end = mid - 1
                else:   # target == mid value
                    ans = mid # potential answer found
                    if findStartIndex: #Ture
                        end = mid - 1 # check from left of middle value
                    else: # False
                        start = mid + 1 # check from left of middle value
            # end of while return the answer to main function
            return ans
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1] 
        ans[0] = self.search(nums,target,True) # fist index
        if ans[0] != -1: # first index is found
            ans[1] = self.search(nums,target,False) #
        return ans # return answer