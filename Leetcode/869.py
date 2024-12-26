#monotonic array
class Solution(object):
    def isMonotonic(self, nums):
        if all(nums[i]>=nums[i+1] for i in range(len(nums)-1)):
          return True
        if all(nums[i]<=nums[i+1] for i in range(len(nums)-1)):
          return True
        else:
            return False
