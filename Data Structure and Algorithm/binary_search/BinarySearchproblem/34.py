def search(nums, target,findStartIndex):
    # answer -1 if not found + start = fist index of list + End lenght of the list - 1
    # ans,start,end = -1,0,(len(nums)-1)
    ans = -1
    start = 0 
    end = len(nums)-1
    print('values:',ans,start,end)
    # check to find middle value as target value
    while start <= end:
        mid = (end+start)//2  # middle value
        print("start,end,mid:",start,end,mid)
        if target > nums[mid]:
            start = mid + 1
            print("start:",start) 
        elif target < nums[mid]:
            end = mid - 1
            print("end:",end)
        elif target == nums[mid]:   # target == mid value
            ans = mid # potential answer found
            print("else asn:",ans)
            if findStartIndex == True: #Ture
                end = mid - 1 # check from left of middle value
                print("Go Left-> end value:",end)
            else: # False
                start = mid + 1 # check from left of middle value
                print("Go Right-> Start value:",start)
    # end of while return the answer to main function
    print('outer while:',ans)
    return ans


def searchRange(nums, target): #main
    ans = [-1,-1] # answer if not found 
    ans[0] = search(nums,target,findStartIndex = True) # fist index
    print("retrin firsrt index:",ans[0]) 
    if ans[0] != -1: # first index is found
        ans[1] = search(nums,target,findStartIndex = False) # lst index 
        print(ans[1]) 
    return ans # return answer

nums = [5,7,7,8,8,10]
target = 7
answer = searchRange(nums,target)
print(answer)