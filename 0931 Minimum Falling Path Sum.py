class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        if col == 1: 
            res = 0 
            for i in range(row):
                res += matrix[i][0]
            return res
        for i in range(1,row):
            for j in range(col):
                if j == col-1 :
                    matrix[i][j] = min(matrix[i-1][j],matrix[i-1][j-1]) + matrix[i][j]
                elif j != 0 :
                    matrix[i][j] = min(matrix[i-1][j-1],matrix[i-1][j],matrix[i-1][j+1]) + matrix[i][j]
                else : 
                    matrix[i][j] = min(matrix[i-1][j],matrix[i-1][j+1]) + matrix[i][j]
                    
        return min(matrix[row-1])
