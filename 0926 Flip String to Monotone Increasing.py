class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        #re
        sz = len(s)
        totalone = s.count('1')
        totalzero = s.count('0')
        if totalone == sz or totalzero == sz : 
            return 0
        zero = 0 
        one = 0
        res = 987564321
        for i in range(sz-1) :
            if s[i] =='0' and s[i+1] == '1' : 
                res = min(res, sz - i - 1 - totalone + 2 * one)
            if s[i] == '0':
                zero += 1
            else : 
                one += 1
        return min(res, sz - s.count('1'), sz - s.count('0'))
