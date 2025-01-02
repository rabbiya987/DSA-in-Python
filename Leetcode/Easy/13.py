class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        x={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum=0
        i=0
        n=len(s)
        while i<n:
            if i<n-1 and x[s[i]]<x[s[i+1]]:
                sum+=x[s[i+1]]-x[s[i]]
                i+=2
            else:
                sum+=x[s[i]]
                i+=1
        return sum
            
