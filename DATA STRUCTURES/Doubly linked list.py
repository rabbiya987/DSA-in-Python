#Creating a class for node
class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

def traverse(head):
        cur=head
        while cur:
            print(cur.data,end=" <-> ")
            cur=cur.next
        
def insert_at_beginning(head,data):
        new_node=Node(data)
        new_node.next=head
        if head:
            head.prev=new_node
        return new_node
    
# Driver Code
head = None
head = insert_at_beginning(head, 4)
head = insert_at_beginning(head, 3)
head = insert_at_beginning(head, 2)
head = insert_at_beginning(head, 1)

# To traverse and print the nodes:
traverse(head)
