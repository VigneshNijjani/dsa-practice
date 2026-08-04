def solve(nums):
    for i in range(len(nums)):
        print(nums[i:]+nums[:i])

nums=[1,2,3,4,5]
solve(nums)