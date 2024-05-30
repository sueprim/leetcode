class Solution:
    def totalMoney(self, n: int) -> int:
        mod = n // 7
        res = n % 7
        ans = 0
        for i in range(mod):
            ans += 28 + i * 7
        for i in range(1,res+1) : 
            ans += i + mod
        return ans  
