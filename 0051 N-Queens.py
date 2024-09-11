class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def promising(i,col):
            k = 0
            switch = True
            while k < i and switch == True :
                if col[i] == col[k] or abs(col[i] - col[k]) == i -k :
                    switch = False
                k+=1
            return switch
        def queens(n,i,col,res): 
            if promising(i,col) : 
                if i == n-1 :
                    size = len(res)
                    res.append([])
                    for j in range(len(col)):
                        resstr = ""
                        find = col[j]
                        for k in range(len(col)):
                            if k ==find :
                                resstr+="Q"
                            else :
                                resstr+="."
                        res[size].append(resstr)
                else:
                    for j in range(0,n):
                        col[i+1] = j
                        queens(n,i+1,col,res)
        col = n *[0]
        res = []
        queens(n,-1,col,res)
        return res  
