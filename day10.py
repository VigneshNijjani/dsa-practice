# max sum of sub arr 

# num=[5,9,1,8,7,8,2,4,5]
# n=len(num)
# max_sum=0
# for i in range(n):
#     sum=0
#     for j in range(i,n):
#         if j-i==2:
#             for k in range(i,j+1):
#                 sum+=num[k]
#         if sum>max_sum:
#             max_sum=sum
# print(max_sum)


# L=[5,9,1,8,7]
# n=len(L)
# l=0
# a=[]
# temp=0
# win_size=3
# for r in range(n):
#     temp+=L[r]
#     if r-l==win_size:
#         temp-=L[l]
#         l+=1    
#     if r-l+1==win_size:
#         a.append(temp)
    
# print(a)


# s="abcaaaabbcc"
# s=set(s)
# print(s)
# a=str(s)
# print("".join(s))


# s="xyzzaz"
# win_size=3
# l=0
# temp=""
# a=[]
# t=0
# for r in range(len(s)):
#     temp+=s[r]
#     if r-l==win_size:
#         temp=temp[1:]
#         l+=1
#     if r-l+1==win_size:
#         a.append(temp)
# print(a)
# for i in a:
#     v=set(i)
#     i="".join(v)
#     if len(i)==win_size:
#         t+=1
# print(t)

# nums=[9,4,1,7]
# win_size=2
# l=0
# temp=0
# ans=float("inf")
# for r in range(len(nums)):
#     temp+=nums[r]
#     if r-l+1>win_size:
#         temp-=nums[l]
#         l+=1
#     if r-l+1==win_size:
#         ans=min(ans,temp)
# print(ans)




