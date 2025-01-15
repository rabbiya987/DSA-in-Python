class Solution(object):
    def search(self, arr, x):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low=0
        high=len(arr)-1
        while low<=high:
            mid=low+((high-low) // 2)
            if arr[mid]==x:# Check if x is present at mid
                return mid
            elif arr[mid]<x:
                low=mid+1  # If x is greater, ignore left half
            else:
                high=mid-1 # If x is smaller, ignore right half
        return -1 #If the element is not found in array 