class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        S=len(s)
        T=len(t)
        if s=='': return True # if the string is empty then it is a substring of t
        if S>T: return False #if the length os s is greater than t it cant be a substring 

        j=0
        for i in range(T):
            if t[i]==s[j]:
                if j==S-1: #if j is the last index of s and it matches t then it is the substring of t in correct order
                    return True
                j+=1
        return False
