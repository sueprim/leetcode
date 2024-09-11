class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0 
        idx = 0 
        mod = 10**9 + 7 
        while idx < len(s)-1:
            temp = 1
            while idx < len(s)-1 and s[idx] == s[idx+1] :
                temp += 1
                idx += 1
            res += temp * (temp + 1) // 2
            idx+=1
            
        if idx != len(s) : 
            res+=1
        return res % mod
