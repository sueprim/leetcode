class Solution:
    def countSegments(self, s: str) -> int:
        if len(s) == 0  or s.count(' ') == len(s) :
             return 0
        res = 0 
        idx = 0 
        while idx < len(s) : 
            if s[idx] != ' ': 
                res += 1
                while idx < len(s) and s[idx] != ' ':
                    idx+=1
            else: 
                idx += 1
        return res    
