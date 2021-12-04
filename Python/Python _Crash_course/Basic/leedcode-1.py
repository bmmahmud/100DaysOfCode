nums = [3,2,4]
target = 6


def twoSum(nums, target):
    for i in range(len(nums)):
        # print('letters', i,' = ',nums)
        numberTofind = target - nums[i]
        # print('i',i,":",nums[i],'numberTofind:',numberTofind)
        for j in range(i+1,len(nums)):
            # print('j',j,':',nums[j])
            if numberTofind == nums[j]:
                # print('j',nums[j],'i',nums[i])
                return [i,j]
            
        return None   
twoSum(nums,target)        



# # def twoSum(nums, target):
# for i in range(len(nums)):
#     # print('letters', i,' = ',nums)
#     numberTofind = target - nums[i]
#     print('i',i,":",nums[i],'numberTofind:',numberTofind)
#     for j in range(i+1,len(nums)):
#         print('j',j,':',nums[j])
#         if numberTofind == nums[j]:
#             print('j',nums[j],'i',nums[i])
#         else: 
#             print("Not Found")            
#     # print("Null")        
    
    
