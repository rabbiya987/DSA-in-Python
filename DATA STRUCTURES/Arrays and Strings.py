#Array 
a=[1,2,3]
print(a)

#Append: Insert an array at the end - O(1)
a.append(5)
print(a)

#Pop: Deleting the last element - O(1)
a.pop()
print(a)

#Insertion: Inserting in middle - O(n)
a.insert(0,4)
print(a)

#Modification: Change the element of any index - O(1)
a[2]=7
print(a)

#Accessing element - O(1)
print(a[2])

#Searching an element in an array - O(n)
if 4 in a:
    print(True)


#String
s="Dauntless"

#Append - O(n) - Because a new string is made to concatenate 
b=s+'123'
print(b)

#Searching an element in string - O(n)
if 'p' in s:
    print(True)
else:
    print(False)

#Accessing element - O(1)
print(s[2])

#Checking length - O(1)
print(len(s))