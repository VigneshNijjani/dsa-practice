# find Maximum Element

# l=[7,25,34,43,5,162,61]

# print(max(l))

# m=float("-inf")
# for i in l:
#     if i>m:
#         m=i
# print(m)
# ----------------------------------------------------------------------------------------------------------------/
# Find Minimum Element

# l=[7,25,34,43,5,162,61]
# m=float("inf")
# for i in l:
#     if i<m:
#         m=i
# print(m)


# ---------------------------------------------------------------------------------------------------------------------------
# Second Largest Element

# l=[7,25,34,43,5,162,61]
# largest=float("-inf")
# secound=float("-inf")

# for i in l:
#     if i>largest:
#         secound=largest
#         largest=i
#     elif i>secound and i !=largest:
#         secound=i
# print(secound)

# ---------------------------------------------------------------------------------------------------------------------------
# Check if Array is Sorted
# l=[7,25,34,43,5,162,61]
# b=sorted(l)

# def sort_check(list):
#     l=list
#     ans="sorted"
#     for i in range(len(l)-1):
#         if l[i]<l[i+1]:
#             pass
#         else:
#             ans="not sorted"
#     return ans
# def sort_check1(list):
#     l=list
#     ans="sorted"
#     for i in range(len(l)-1):
#         if l[i]>l[i+1]:
#             pass
#         else:
#             ans="not sorted"
#     return ans
# if sort_check1(l)=="sorted" or sort_check(l)=="sorted":
#     print("sorted")
# else:
#     print("not sorted") 

# ---------------------------------------------------------------------------------------------------------------------
# Remove Duplicates from Sorted Array

# l=[43,5,162,61,25,34,47,25,34,43,5,162,61,25,34,43,5,162]

# print(sorted(set(l)))

# ------------------------------------------------------------------------------------------------------------------------
# Left Rotate Array by One

# l=[1,2,3,4,5]

# k=2
# k=k%len(l)
# print(l[k:]+l[:k])

# k=2
# k=k%len(l)

# while k!=0:
#     l.append(l.pop(0))
#     k-=1
# print(l)

# ---------------------------------------------------------------------------------------------------------------------------------
# Right Rotate Array by One

# l=[1,2,3,4,5]
# k=7
# k=k%len(l)

# print(l[-k:]+l[:-k])

# while k!=0:
#     l.insert(0,l.pop())
#     k-=1
# print(l)

# Reverse an Array
# -----------------------------------------------------------------------------------------------------------------------------------

# l=[1,2,3,4,5]
# i=0
# j=len(l)-1

# while i<j:
#     l[i],l[j]=l[j],l[i]
#     i+=1
#     j-=1
# print(l)

# Two Sum
# target=5
# pairs=[]
# l=[0,1,2,3,4,5,6,7]


# for i in (l):
#     for j in(l):
#         if i+j==target:
#             if (i,j)and(j,i) not in pairs:
#                 pairs.append((i,j))
# print(pairs)

# map={}
# for i in l:
#     if i in map:
#         pairs.append((i,map[i]))
#     diff=target-i
#     map[diff]=i
    
# print(pairs)

# Best Time to Buy and Sell Stock
# profit = 0
# buy = 0
# sell = 0

# l = [7, 1, 5, 3, 6, 4]
# n = len(l)

# for i in range(n):
#     for j in range(i + 1, n):
#         if l[j] - l[i] > profit:
#             profit = l[j] - l[i]
#             buy = i
#             sell = j

# print(buy, sell)
# print(profit)

# Contains Duplicate
# l=[4, 2, 7, 2]
# b=set(l)
# if len(l)==len(b):
#     print("no duplicates")
# else:
#     print("duplicates")

# Missing Number

# l=[9,6,4,2,3,5,7,0,1]
# m=max(l)
# flag=0
# for i in range(m+1):
#     if i not in l:
#         flag=1
#         print(i)
#         break
# if flag==0:
#     print(m+1)
    
# Single Number
# d={}
# l=[4,1,2,1,2]
# for i in l:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# for i in d:
#     if d[i]==1:
#         print(i)

# Move Zeroes
# i=0
# j=0
# l=[0,0,1,22,0,4,6,0,6,2,0]
# while j<len(l):
#     if l[j]!=0:
#         l[j],l[i]=l[i],l[j]
#         i+=1
#     j+=1
# print(l)

# Plus One
# l=[1,2,9,9,9,9]
# carry=0
# flag=0
# n=len(l)-1
# while n>=0:
#     if carry==0 and flag==0:
#         flag=1
#         l[n]=l[n]+1 
#         if l[n] ==10:
#             l[n]=0
#             carry=1
#     elif carry==1:
#         l[n]+=1
#         carry=0
#         if l[n]==10:
#             l[n]=0
#             carry=1   
#     n-=1
# if carry==1:
#     l.insert(0,1)
# print(l)

# Majority Element
# maxi=0
# flag=0
# d={}
# l=[4,1,2,1,2,1,5,6,6,6,6,6]
# for i in l:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# for i in d:
#     if flag==0:
#         maxi=i
#         flag=1
#     elif d[i]>d[maxi]:
#         maxi=i
# print(maxi)
    
# Running Sum of 1D Array


# l=[1,2,3,4]
# sum=0
# for i in range(len(l)):
#     l[i]=l[i]+sum
#     sum=l[i]
# print(l)


# Find Pivot Index

# l = [1,7,3,6,5,6]
# total=sum(l)
# left=0
# flag=0
# for i in range(len(l)):
#     right=total-left-l[i]
#     if left==right:
#             flag=1
#             print(i)
#             break
#     left+=l[i]
# if flag==0:
#     print(-1)

# Range Sum Query – Immutable
# def solve1(list,left,right):
#     sum=0
#     for i in range(left,right+1): 
#         sum+=list[i]
#     return sum
# nums = [-2,0,3,-5,2,-1]
# print(solve1(nums,2,5))

# nums=  [-2,0,3,-5,2,-1]
# pre=[]#[-2,-2,1,-4,-2,-3]
# sum=0
# for i in nums:
#     sum+=i
#     pre.append(sum)
# def solve(left,right):
#     # print(pre,pre[right],pre[left])
#     if left==0:
#         sum1=pre[right]
#     else:
#         sum1=pre[right]-pre[left]
#     return sum1 
# print(solve(2,5))


# Find Highest Altitude
# l=[-5,1,5,0,-7]
# max_altitude=0
# altitude=0
# for i in l:
#     altitude+=i
#     if altitude>max_altitude:
#         max_altitude=altitude
# print(max_altitude)

# Maximum Average Subarray I


# Maximum Subarray (Kadane's Algorithm)

# l=[10,20,30,40]
# max_sum=float("-inf")
# cur_sum=0
# for i in l:
#     cur_sum+=i
#     if cur_sum<0:
#         cur_sum=0
#     elif cur_sum>max_sum :
#         max_sum=cur_sum
   
# print(max_sum)


# --------------------------------------------------------------------------------------------------