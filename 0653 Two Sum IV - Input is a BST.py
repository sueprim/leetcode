# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        dic = {}
        def dfs(root):
            if root : 
                dic[root.val] = 1
                dfs(root.left)
                dfs(root.right)
                
        dfs(root)
        if len(dic) == 1 : 
            return False
        for i in dic : 
            if k - i != i and (k - i   in dic) : 
                return True
        return False
