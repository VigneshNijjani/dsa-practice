# nums = [1,2,3,1]  #OUTPUT 4
# Explanation:
# Rob house 1 (1) and house 3 (3).
# 1 + 3 = 4



# nums = [2,7,9,3,1]  #Output:12
# Explanation:
# Rob houses containing:
# 2 + 9 + 1 = 12


def rober(nums):
    def helper(index,memo):
        if index in memo:
            return memo[index]
        if index>=len(nums):
            return 0
        memo[index]= max(nums[index]+helper(index+2,memo),helper(index+1,memo))
        
        return memo[index]
     
    return helper(0,{})
    
    


print(rober([1,2,3,1]))