class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zero = 0
        one = 0
        count = 0 
        i = 0
        while i < len(s):
            while i < len(s) and s[i] == "0"  : 
                i+=1
                count+=1
            zero = max(zero,count)
            count= 0
            while i<len(s) and s[i] == "1" :
                i+=1
                count+=1
            one = max(one,count)
            count= 0 
        return one>zero    
