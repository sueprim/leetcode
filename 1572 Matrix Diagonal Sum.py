class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sz = len(mat)
        res = 0
        for i in range(sz) : 
            res += mat[i][i] + mat[i][sz-i-1]
        return res if sz % 2 == 0 else res - mat[sz//2][sz//2]
