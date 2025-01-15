class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashmap = {")": "(", "}": "{", "]": "["}
        stk=[]
        for x in s:
            if x not in hashmap:
                stk.append(x)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != hashmap[x]:
                        return False

        return not stk

            