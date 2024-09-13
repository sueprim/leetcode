dx=[-1,0,1,0]
dy=[0,1,0,-1]
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def BFS(i,j,row,col,grid,v):
            area = 1
            dq = deque()
            dq.append([i,j])
            v[i][j] = 1
            while dq : 
                x,y = dq.popleft()
                for k in range(4):
                    newx,newy = x+dx[k], y+dy[k]
                    if 0<=newx and newx<row and 0<=newy and newy<col and grid[newx][newy] == 1 and v[newx][newy] == 0 :
                        v[newx][newy] = 1
                        dq.append([newx,newy])
                        area+=1
            return area
        row = len(grid)
        ans = 0
        col = len(grid[0])
        v = [0] * row
        for i in range(row) : 
            v[i] = [0] * col
        
        for i in range(row) : 
            for j in range(col):
                if grid[i][j] == 1 and v[i][j] ==0:
                    ans = max(ans,BFS(i,j,row,col,grid,v))
        return ans
