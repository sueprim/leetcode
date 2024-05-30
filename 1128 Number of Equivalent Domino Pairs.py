class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        check = [[0] * 10 for i in range(10)]
        result = 0
        for i in range(len(dominoes)) :
            x,y = dominoes[i][0], dominoes[i][1]
            if x > y : 
                check[y][x] += 1
            else : 
                check[x][y] += 1
                
        for i in range(10) : 
            for j in range(10) :
                if check[i][j] >1 : 
                    result += (check[i][j] *(check[i][j]-1)) //2
        return result
