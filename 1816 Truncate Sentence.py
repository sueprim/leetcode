class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        splitlist = s.split()
        res=""
        for i in range(k):
            res+=splitlist[i]+" "
        return res[:-1]
