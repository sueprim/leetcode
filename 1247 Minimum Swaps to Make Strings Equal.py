class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xcount = 0 
        ycount = 0 
        res = 0 
        for i in range(len(s1)) : 
            if s1[i] != s2[i] : 
                if s1[i] == 'x' : 
                    xcount += 1
                else :
                    ycount += 1
        if (xcount + ycount) % 2 == 1: 
            return -1
        else : 
            res = (xcount // 2) + (ycount // 2) 
            if xcount %2 == 1 : 
                res += 2
        return res
