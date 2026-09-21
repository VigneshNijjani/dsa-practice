# l=[]
# count=0
# n=int(input())
# for i in range(n):
#     arr=list(map(int,input().split()))
#     l.append(arr)
# for i in l:
#     for j in i:
#         if j<0:
#             count+=1
# print(count)



# stack

# class Stack:
#     def __init__(self):
#         self.arr=[]

#     def push(self,x):
#         self.arr.append(x)

#     def pop(self):
#         if len(self.arr)==0:
#             return -1
#         x=self.arr.pop()
#         return x

#     def peek(self):
#         if len(self.arr)==0:
#             return -1
#         x=self.arr[-1]
#         return x

#     def isempty(self):
#         if len(self.arr)==0:
#             return True
#         return False


# queue
# class Queue:
#     def __init__(self):
#         self.arr=[]

#     def enqueue(self,x):
#         self.arr.append(x)

#     def dequeue(self):
#         if len(self.arr)==0:
#             return -1
#         self.start=0
#         return self.arr.popleft()

#     def front(self):
#         if len(self.arr)==0:
#             return -1
#         return self.arr[0]

#     def rear(self):
#         if len(self.arr)==0:
#             return -1
#         return self.arr[-1]

#     def isempty(self):
#         if len(self.arr)==0:
#             return True
#         return False

    
# linkedlist