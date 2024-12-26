#K-th Grammer 
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return (k - 1).bit_count() & 1

obj=Solution()    
print(obj.kthGrammar(2,2))