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


def johnson_order(a, b):
    n = len(a)

    jobs = list(range(n))

    # Johnson's Rule
    jobs.sort(key=lambda i: (
        0 if a[i] <= b[i] else 1,
        a[i] if a[i] <= b[i] else -b[i]
    ))

    return jobs


def completion_time(order, a, b, removed):
    station1 = 0
    station2 = 0

    for i in order:
        station1 += a[i]

        if i == removed:
            current_b = 0
        else:
            current_b = b[i]

        station2 = max(station2, station1) + current_b

    return station2


def solve():
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    order = johnson_order(a, b)

    ans = float('inf')

    for removed in range(n):
        # Removed b[i] becomes 0.
        # It should be placed at the end.
        remaining = [i for i in order if i != removed]
        remaining.append(removed)

        time = completion_time(remaining, a, b, removed)

        ans = min(ans, time)

    print(ans)


solve()