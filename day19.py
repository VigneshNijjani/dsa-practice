def getFinalState(nums,k,multiplier):
    for i in range(k):
        x=float("inf")
        ind=0 
        for j in range(len(nums)):
            if nums[j]<x:
                x=nums[j]
                ind=j
        nums[ind]=nums[ind]*multiplier
    return nums
print(getFinalState(nums = [2,1,3,5,6], k = 5, multiplier = 2))