class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        h=set()
        for x in nums:
            if x in h:
                return True
            else:
                h.add(x)
        return False

        