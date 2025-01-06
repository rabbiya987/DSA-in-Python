class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        j=set(jewels)
        sum=0
        for x in stones:
            if x in j:
                sum+=1
        return sum
