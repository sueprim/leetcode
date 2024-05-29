class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def DFS(root,targetSum,curr):
            if root: 
                curr += root.val
                if curr == targetSum and root.left == None and root.right == None: 
                    return True
                return DFS(root.left,targetSum,curr) or DFS(root.right,targetSum,curr)
        return DFS(root,targetSum,0)
