class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat):
            new = copy.deepcopy(mat)
            for i in range(len(mat)):
                for j in range(len(mat[i])):
                    new[j][len(mat[i]) - i - 1] = mat[i][j] 
            return new
        for i in range(4):
            if mat == target : 
                return True
            mat = rotate(mat)
        return False
