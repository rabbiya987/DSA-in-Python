#Creating class for Node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#Creating a class for Stack  
class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

        # String representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.data) + "->"
            cur = cur.next
        return out[:-2]
    

    #Return the size of stack
    def size(self):
        return self.size
    
    # Check if the stack is empty
    def isEmpty(self):
        return self.size==0
    
    # Get the top item of the stack
    def peek(self):
        if self.isEmpty():
            return None
        
        return self.head.next.value
    
        # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head.next # Make the new node point to the current head
        self.head.next = node #!!! # Update the head to be the new node
        self.size += 1


    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = remove.next #!!! changed
        self.size -= 1
        return remove.data


if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")

    for _ in range(1, 6):
        top_value = stack.pop()
        print(f"Pop: {top_value}") # variable name changed
    print(f"Stack: {stack}")

    
