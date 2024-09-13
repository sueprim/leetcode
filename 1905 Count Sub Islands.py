class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row = len(grid2)
        col = len(grid2[0])
        res = 0
        dx =[-1,0,1,0]
        dy = [0,-1,0,1]
        v = [0] * row
        for i in range(row) : 
            v[i] = [0] * col
        for i in range(row) : 
            for j in range(col):
                if v[i][j] == 0 and grid2[i][j] == 1 :
                    if grid1[i][j] == 0 :
                        continue
                    else : 
                        dq = deque()
                        dq.append((i,j))
                        v[i][j] = 1
                        check = False
                        while dq : 
                            x,y = dq.popleft()
                            for k in range(4) : 
                                newx,newy = x + dx[k] , y + dy[k]
                                if 0<= newx and newx <row and 0 <= newy and newy < col and grid2[newx][newy] == 1:
                                    if v[newx][newy] == 1 :
                                        continue
                                    else : 
                                        if grid1[newx][newy] == 0 : 
                                            check = True
                                        dq.append((newx,newy))
                                        v[newx][newy] = 1    
                        if check == False : 
                            res+=1
        return res
