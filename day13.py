class node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=node(10)
head.next=node(20)
head.next.next=node(30)

# traversal

curr=head
while curr:
    print(curr.data,end="->")
    curr=curr.next
print("Null")

# inserting at start 

# accorinding to above program linkedlist till now is 10->20->30->null

new_node=node(0)
new_node.next=head
head=new_node

# traversing agin
# befor linked list is 10->20->30->Null
curr=head
while curr:
    print(curr.data,end="->")
    curr=curr.next
print("Null")

# now linked list is 0->10->20->30->Null


# deleting a kay or node lets say 30

key=30
curr =head
prev=None
while curr and curr.data != key:
    prev=curr
    curr=curr.next

# only used if you want to delete head node
if head==curr:
    head=head.next
elif curr:
    prev.next=curr.next


curr =head
while curr:
    print(curr.data,end="->")
    curr=curr.next
print("Null")
