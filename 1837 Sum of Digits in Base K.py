class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = ""
        while n :
            res += str(n % k)
            n = n // k
        sumres = 0 
        for i in range(len(res)):
            sumres += int(res[i])
        return sumres
