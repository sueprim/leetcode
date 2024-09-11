class Solution:
    def countNegatives(self,grid):
        count = 0 
        grid_sum = sum(grid, [])
        for i in grid_sum:
            if i < 0:
                count += 1
        return count
