#List - They are mutable
list=[1,2,'abc',4]

#Multidimensional list
list2=[[1,2,3],['a','b','c']]
print("Multidmensional List: ",list2)

#Adding an element at the end
list.append(11)
print("\nAdded an element: ",list)

#Insert in the middle
list.insert(2,'hi')
print("\nInsert an element: ",list)

#Adding multiple elements at the end
list.extend(['a','b',77])
print("\nAdded elements: ",list)

#Remove an element
list.remove(1)
print("Remove an element: ",list)

#Accessing elements
print("\nAccessing element using index: ",list[1])

#using -ve index
print("\nAccessing element using -ve index: ",list[-1])

#TUPLE - They are immutable
tuple1=('abc','def')
print("\nTuple: ",tuple1)

#Creating tuple using a given list
Tuple2=tuple(list)
print("\nTuple created using list: ",Tuple2)

#Concatenating tuples
t3=tuple1+Tuple2
print("Conacatenate 2 tuples",t3)

# Accessing element using indexing
print("\nFirst element of tuple:",Tuple2[0])

# Accessing element from last negative indexing
print("\nLast element of tuple:",Tuple2[-1])
