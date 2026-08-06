# def solve(nums):
#     for i in range(len(nums)):
#         print(nums[i:]+nums[:i])

# nums=[1,2,3,4,5]
# solve(nums)

def firstMissingPositive(nums):
        flag=0
        for i in range(1,max(nums)):
            if i not in nums:
                flag=1
                print(i)
        if flag==0:
            print(max(nums)+1,flag) 
nums=[3,-4,1,-1]
firstMissingPositive(nums)