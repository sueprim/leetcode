class Solution:
    def countTriples(self, n: int) -> int:
        dic = {}
        res = 0 
        for i in range(1,n+1) :
            dic[i**2] = 1
        for i in range(n,1,-1) : 
            for j in range(i-1,0,-1):
                if (i**2) - (j**2) in dic : 
                    res+=1
        return res
