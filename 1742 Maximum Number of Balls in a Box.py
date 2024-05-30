class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        res = [0] * 100
        ans = 0
        for i in range(lowLimit,highLimit+1):
            #brute
            temp = str(i)
            sumnum = 0 
            for k in range(len(temp)):
                sumnum += int(temp[k])
            res[sumnum] += 1 
            ans = max(ans,res[sumnum])
        return ans
