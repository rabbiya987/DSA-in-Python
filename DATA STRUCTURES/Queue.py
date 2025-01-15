from collections import deque
q = deque()

#Append -O(1)
q.append('a')
q.append('b')
q.append('c')

print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
#Pop-O(1)
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)