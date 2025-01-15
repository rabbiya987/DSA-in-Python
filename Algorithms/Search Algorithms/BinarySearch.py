def binarysearch(arr, low, high, x):
    while low<=high:
        mid=low+((high-low) // 2)
        if arr[mid]==x:# Check if x is present at mid
            return mid
        elif arr[mid]<x:
            low=mid+1  # If x is greater, ignore left half
        else:
            high=mid-1 # If x is smaller, ignore right half
    return -1 #If the element is not found in array 
    
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    # Function call
    result = binarysearch(arr, 0,len(arr)-1,x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")   
