# l=[[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         print(i,j)
#         l[j][i],l[i][j]=l[i][j],l[j][i]
# for i in l:
#     i.reverse()
# print(l)

# def titleToNumber( columnTitle: str) -> int:
#         alphabets=26
#         a=columnTitle[-1]
#         print(a)
#         b=len(columnTitle)
#         if b==1:
#             return ((ord(a)+(alphabets**b))-90)
#         else:
#             return ((ord(a)+(alphabets**b))-64)
            

# print(titleToNumber("AB"))
# # print(26*26+25)
# # print(-64)


# # (ord(a)+(alphabets*b)-64)




# def digitFrequencyScore( n: int) -> int:
#     sum=0
#     d={}
#     while n!=0:
#         rem=n%10
#         if rem in d:
#             d[rem]+=1
#         else:
#             d[rem]=1
#         n//=10
#     for i,j in d.items():
#         sum+=i*j
#     return sum
# print(digitFrequencyScore(101))

# n=15
# if n%10==5:
#     n+=1
# n/=10
# n=round(n)
# print(n)
# # if n==1:
# #     pass
# # else:
# n*=10
# print(100-n)

s="aabaa"
print(s[::-1],s[::])