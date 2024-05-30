class Solution:
    def minOperations(self, s: str) -> int:
        # start 0
        # start 1
        checknum = 0 
        for i in range(len(s)):
            if i%2 == 0 :
                if s[i] == "0": 
                    continue
                checknum += 1
            else : 
                if s[i] =="1":
                    continue
                checknum += 1
        return min(checknum, len(s) - checknum)
