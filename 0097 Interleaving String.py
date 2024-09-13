class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        row = len(s1)+1
        col = len(s2)+1
        if row + col-2 != len(s3)  : 
            return False
        DP = [0] * (row)
        for i in range(row) : 
            DP[i] = [0] * (col)
        for i in range(row) : 
            for j in range(col):
                if i == 0 and j == 0:
                    DP[i][j] = 1
                elif i == 0 :
                    DP[i][j] = (1 if DP[i][j-1] and s2[j-1] == s3[i+j-1] else 0)
                elif j == 0:
                    DP[i][j] = (1 if DP[i-1][j] and s1[i-1] == s3[i+j-1] else 0)
                else : 
                    DP[i][j] = 1 if (DP[i-1][j] and s1[i-1] == s3[i+j-1]) or (DP[i][j-1] and s2[j-1] == s3[i+j-1]) else 0
        return DP[row-1][col-1]
