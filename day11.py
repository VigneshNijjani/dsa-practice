# class linkedlist:
#     def __init__(self,value=None,next=None):
#         self.value=value
#         self.next=next

#     def __str__(self):
#         return str(self.value)

# head=linkedlist(1)
# a=linkedlist(2)
# b=linkedlist(3)
# c=linkedlist(4)
# d=linkedlist(5)

# head.next=a
# a.next=b
# b.next=c
# c.next=d

# def display(head):
#     print(str(head))
#     l=[]
#     curr=head
#     while curr:
#         l.append(str(curr))
#         curr=curr.next
#     print("->".join(l))
# display(head)



def arrayPairSum( nums: List[int]) -> int:
    nums.sort()
    ans=0
    for r in range(len(nums)):
        if r%2==0:
            ans+=nums[r]
    return ans




