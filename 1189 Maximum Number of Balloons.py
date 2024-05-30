class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        res = 987654321
        res = min(text.count('b'),res)
        res = min(text.count('a'),res)
        res = min(text.count('l')//2,res)
        res = min(text.count('n'),res)
        return min(res,text.count('o')//2) 
