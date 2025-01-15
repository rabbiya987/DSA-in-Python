def linearsearch(arr,y):
    N = len(arr)
    for x in range(0,N):
   
        if arr[x]==y:
            return x
    return -1
        
if __name__=="__main__":
    arr=[12,33,22,55,21]
    z=33
    result=linearsearch(arr,z)
    if result==-1:
        print("Element not found")

    else:
        print("Elemnt is present at index:",result)
