#METHOD1 Brute Force Solution( Squaring and sorting)
def sorted_squared(array):
    new_array=[0]*len(array)
    for i in range(len(array)):
        new_array[i]=array[i]**2
    new_array.sort()
    return new_array


print(sorted_squared([-4,-1,0,3,10]))

#METHOD2(Using 2 Pointers)
def sorted(array):
    n=len(array)
    i,j=0,n-1
    res=[0]*n
    for k in reversed(range(n)):
        if array[i]**2>array[j]**2:
            res[k]=array[i]**2
            i+=1
        else:
            res[k]=array[j]**2
            j-=1
    return res

print(sorted([1,2,3,4]))

#METHOD3
class Solution:
    def sorted(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([x ** 2 for x in A])
obj=Solution()
print(obj.sorted([1,0,3,4]))
