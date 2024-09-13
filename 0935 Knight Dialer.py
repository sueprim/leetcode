class Solution:
    def knightDialer(self, n: int) -> int:
        x0 = x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = 1
        for i in range(n-1) : 
            x0,x1,x2,x3,x4,x6,x7,x8,x9 = \
            x4 + x6, x6 + x8, x7 + x9,\
            x4 + x8, x3 + x0 + x9, x0 + x1 + x7,\
            x2 + x6, x1 + x3, x2 + x4
            
            
        res = x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9
        if n != 1: 
            res-=1
        return (res) % (10**9 + 7)
