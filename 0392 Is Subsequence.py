class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        cnt = 0
        if len(s) == 0:
            return True

        for i in t:
            if i == s[idx]:
                idx += 1
                cnt += 1
                if len(s) == cnt:
                    break    
        
        if cnt == len(s):
            return True
        else:
            return False
