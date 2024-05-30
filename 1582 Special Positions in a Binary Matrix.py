class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def checkj(mat,j):
            i = 0 
            sumres = 0 
            while i < len(mat) : 
                if mat[i][j] == 1 :
                    sumres += 1
                    if sumres > 1 : 
                        return 2
                i += 1
            return 1
                
        row = len(mat)
        col = len(mat[0])
        res = 0
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1 and sum(mat[i]) == 1 and checkj(mat,j) == 1 :
                    res += 1
        return res
