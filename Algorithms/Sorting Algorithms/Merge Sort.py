def merge_sort(array):
    if 1>=len(array):
        return array
    mid=len(array)//2
    left_arr=array[:mid]
    right_arr=array[mid:]

    left_arr=merge_sort(left_arr)
    right_arr=merge_sort(right_arr)

    return merge(left_arr,right_arr)

def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i<len(left):
        result.append(left[i])
        i+=1

    while j<len(right):
        result.append(right[j])
        j+=1

    return result

array =[3,62,5,5,4,7]
print(merge_sort(array))