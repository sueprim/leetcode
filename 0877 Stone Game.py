class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        piles.sort()
        dq = deque(piles)
        alex = 0
        lee = 0
        while dq : 
            alex += dq.pop()
            lee += dq.pop()
        return True if alex > lee else False
