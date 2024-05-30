class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if len(s) == 1 :
            return True
        for i in range(len(s)-1,0,-1):
            if s[i] == "1" and s[i-1] == "0" :
                return False
        return True  
