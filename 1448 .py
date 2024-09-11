# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = [0]
        def dfs(root : TreeNode, sd,result) -> int : 
            if root : 
                if sd <= root.val : 
                    sd = root.val
                    result[0] += 1
                    print(result,root.val,sd)
                dfs(root.left,sd,result) 
                dfs(root.right,sd,result)
        dfs(root,root.val,result)
        return result[0]
