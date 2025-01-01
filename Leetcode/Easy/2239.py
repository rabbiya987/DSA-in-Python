class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Assuming that value at index 0 is smallest.
        closest=nums[0]
        #Comparing all the the values 
        for r in nums:
            if abs(r)<abs(closest):
                closest=r
        if closest<0 and abs(closest) in nums:
                return abs(closest)
        else:
            return closest