def selection_sort(nums):
    for i in range(len(nums)):
        small=i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[small]:
                small=j 
        if i!=small:
                nums[i],nums[small]=nums[small],nums[i]
    return nums

array =[3,62,5,5,4,7]
print(selection_sort(array))