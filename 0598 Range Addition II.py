class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0 :
            return m * n
        minrow = 10**5
        mincol = 10**5
        for i in range(len(ops)):
            minrow = min(ops[i][0],minrow)
            mincol = min(ops[i][1],mincol)
        return minrow * mincol
