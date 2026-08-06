# linked list 
# ---------------------------------------------------------------------------------------------------------


# single linled list 

class single_node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

    def __str__(self):
        return str(self.val)

#inserting data in single linked list

head=single_node(1)
a=single_node(2)
b=single_node(3)
c=single_node(4)
d=single_node(5)

#passing next node as reference like head->next->next->none

head.next=a
a.next=b
b.next=c
c.next=d
# ----------------------------------------------------------------------------------------------------------------------------------------

# iterating through linked lists

def display(head):
    current_node=head
    while current_node:
        print(current_node)
        current_node=current_node.next
display(head)
# =====================================================================
#  or even better display option
# =====================================================================

def display(head):
    current_node=head
    data=[]
    while current_node:
        data.append(str(current_node))
        current_node=current_node.next
    print(" -> ".join(data))
display(head)

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# double linked list

class double_linked_list:
    def __init__(self,val,next=None,prev=None):
        self.val=val
        self.next=next
        self.prev=prev

    def __str__(self):
        return str(self.val)

##inserting data in double linked list

head=double_linked_list(10)
a=double_linked_list(20)
b=double_linked_list(30)
c=double_linked_list(40)

##passing next node as reference like head<->next<->next<->none

head.next=a
a.next=b
a.prev=head
b.next=c
b.prev=a
c.prev=b


def display(head):
    current_node=head
    data=[]
    while current_node:
        data.append(str(current_node))
        current_node=current_node.next
    print(" <-> ".join(data))
display(head)






# inserting elements in double linked list at head place 
#                              or 
# inserting element at head position of double linked lists

def insert_at_head(head,val):
    head,tail=insert_at_head()
    new_node=insert_at_head(head,5)
    new_node.next=head
    head.prev=new_node






