class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        size1 = len(word1)
        size2 = len(word2)
        i = 0
        j = 0
        res = ""
        while i + j < size1 + size2:
            if i < size1 : 
                res += word1[i]
                i+=1
            if j < size2 : 
                res += word2[j]
                j+=1
                
        return res    
