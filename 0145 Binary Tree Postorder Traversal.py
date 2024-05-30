class Solution:
    def dfs(self,root,res) :
        if root : 
            self.dfs(root.left,res)
            self.dfs(root.right,res)
            res.append(root.val)
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res= []
        self.dfs(root,res)
        return res
