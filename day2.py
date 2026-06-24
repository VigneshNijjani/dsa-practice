# # move zeros to end
# l=[0,1,0,2,3,0,0,4]
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[j]==0:
#             l[j],l[i]=l[i],l[j]
# print(l)

# # 2nd way
# l=[0,0,0,1,2,3,0,0,0,0,4,0,5]
# i=0
# j=0
# while j<len(l):
#     if l[j]!=0:
#         l[i],l[j]=l[j],l[i]
#         i+=1
#     j+=1
# print(l)




# l=[1,0,2,3,0,1,4,0,5]
# i=0
# j=0
# while j<len(l):
#     if l[j]!=0:
#         l[i],l[j]=l[j],l[i]
#         i+=1
#         # here not else block becase j+=1 has to be done even if it is zero or non zero 
#     j+=1
# print(l)
