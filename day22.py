# a=10
# b=10
# print(a is b)

# c=[1]
# d=[1]
# print(c is d)

# e=c
# print(e is c)




# shallow copy
print("shallow copy")
l1=[1,2,3,[4,5],6,7]
l2=l1.copy()
print("l1=",l1)
print("l2=",l2)
print()

print("inserting")
l1.append(8)
print("l1=",l1)
print("l2=",l2)
print()

print("assigning")
l1[0]=0
print("l1=",l1)
print("l2=",l2)
print()

# nestedlist difference
print("assigning at nested")
l1[3][0]=44
print("l1=",l1)
print("l2=",l2)
print()

import copy

print("deep copy")
l1=[1,2,3,[4,5],6,7]
l2=copy.deepcopy(l1)
print("l1=",l1)
print("l2=",l2)
print()

print("inserting")
l1.append(8)
print("l1=",l1)
print("l2=",l2)
print()

print("assigning")
l1[0]=0
print("l1=",l1)
print("l2=",l2)
print()

# nestedlist difference
print("assigning at nested")
l1[3][0]=44
print("l1=",l1)
print("l2=",l2)
print()
