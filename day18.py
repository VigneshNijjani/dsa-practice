# def climbing(n):
#     def helper(index,memo):
#         if index==n:
#             return 1
#         if index>n:
#             return 0
#         if index in memo:
#             return memo[index]
#         memo[index+1]=helper(index+1,memo)
#         memo[index+2]=helper(index+2,memo)
#         return helper(index+1,memo)+helper(index+2,memo)
#     return helper(0,{})
# print(climbing(2))

        
# def sumDigitDifferences(nums):
#     ans=0
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             temp=nums[:]
#             while temp[i]!=0 and temp[j]!=0:
#                 if temp[i]%10 != temp[j]%10:
#                     ans+=1
#                 temp[i]//=10
#                 temp[j]//=10
#     print(ans)
# sumDigitDifferences([13,23,12])


# def minCostClimbingStairs(cost):
#     def helper(index,memo):
#         if index >=len(cost):
#             return 0
#         if index in memo:
#             return memo[index]
#         memo[index]=min(cost[index]+helper(index+1,memo),cost[index]+helper(index+2,memo))
#         return memo[index]
#     return min(helper(0,{}),helper(1,{}))
# print(minCostClimbingStairs([10,15,20]))


# def numDistinct(s,t):
#     def helper(index,j):
#         if j ==len(t):
#             return 1
#         if index==len(s):
#             return 0
#         if s[index]==t[j]:
#             pick=helper(index+1,j+1)
#             skip=helper(index+1,j)
#             return pick+skip
#         return helper(index+1,j)
#     return helper(0,0)
# print(numDistinct(s = "rabbbit", t = "rabbit"))