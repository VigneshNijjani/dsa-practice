class node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=node(10)
head.next=node(20)
head.next.next=node(30)

curr=head
while curr:
    print(curr.data,end="->")
    curr=curr.next
print("Null")