# Create a Node class to create a node
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

#Function to add a node at the begining of the list
    def insertatbegin(self,data):
        new_node=node(data)
        if self.head is None:
            self.head= new_node
        else:
            new_node.next=self.head
            self.head=new_node

#Function to add a node at the middle of the list
    def Insert(self,data,index):
        if index == 0:
            self.insertatbegin(data)
            return

        position = 0
        current_node = self.head
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            new_node = node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")
    
#Function to add a node at the end of the list:
    def insertatend(self,data):
        new_node=node(data)
        #If the head is empty make the new node head
        if self.head is None:
            self.head=new_node
            return

        #we make a current_node equal to the head traverse to the last node of the linked list and when we get None after the current_node the while loop breaks and insert the new_node in the next of current_node which is the last node of linked list.
        current_node=self.head
        while current_node.next:
            current_node=current_node.next

        current_node.next=new_node

    #Modify a node
    def modify(self,val,index):
        current_node=self.head
        position=0
        while current_node is not None and position!=index:
            current_node=current_node.next
            position+=1

        if current_node is not None:
            current_node.data=val
        else:
            print("Index not available...... ")

        
    #Remove a first node
    def remove(self):
        if self.head is None:
            return
        self.head=self.head.next

    #Remove the last node:
    def remove_last(self):
        if self.head is None:
            return
        
        # If there's only one node
        if self.head.next is None:
            self.head = None
            return
        
        #Find the second last node of the list
        current_node=self.head
        while current_node.next and current_node.next.next:
            current_node=current_node.next
        
        current_node.next=None

    # Method to remove a node at a given index
    def remove_at_index(self, index):
        if self.head is None:
            return

        if index == 0:
            self.remove_first_node()
            return

        current_node = self.head
        position = 0
        while current_node is not None and current_node.next is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None and current_node.next is not None:
            current_node.next = current_node.next.next
        else:
            print("Index not present")

    #Remove the node through its data
    def remove_by_data(self,data):
        current_node=self.head
        current_node = self.head

        # If the node to be removed is the head node
        if current_node is not None and current_node.data == data:
            self.remove_first_node()
            return

        # Traverse and find the node with the matching data
        while current_node is not None and current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

        # If the data was not found
        print("Node with the given data not found")

        #Print the size of Linked List
    def size(self):
            size=0
            current_node=self.head
            while current_node:
                size+=1
                current_node=current_node.next

            return size
        
         # Print the linked list
    def printLL(self):
           current_node = self.head
           while current_node:
                print(current_node.data)
                current_node = current_node.next

# create a new linked list
llist = LinkedList()   

llist.insertatbegin('s')
llist.insertatend('d')
llist.insertatend('d')
llist.insertatbegin('f')
llist.Insert('s',2)

# print the linked list
print("Node Data:")
llist.printLL()

# remove nodes from the linked list
print("\nRemove First Node:")
llist.remove()
llist.printLL()

print("\nRemove Last Node:")
llist.remove_last()
llist.printLL()

print("\nRemove Node at Index 1:")
llist.remove_at_index(1)
llist.printLL()

# print the linked list after all removals
print("\nLinked list after removing a node:")
llist.printLL()

print("\nUpdate node Value at Index 0:")
llist.modify('z', 0)
llist.printLL()

print("\nSize of linked list:", llist.size())


        




        