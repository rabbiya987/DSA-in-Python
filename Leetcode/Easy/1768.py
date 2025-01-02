class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        A,B=len(word1), len(word2)
        x,y=0,0
        s=[]
        word=1

        while x<A and y<B:
            if word==1:
                s.append(word1[x])
                x+=1
                word=2
            if word==2:
                s.append(word2[y])
                y+=1
                word=1

        while x<A:
            s.append(word1[x])
            x+=1

        while y<B:
            s.append(word2[y])
            y+=1

        return "".join(s)
            
obj=Solution()
print(obj.mergeAlternately("abc","pqrs"))
