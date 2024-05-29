class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root :
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            return left + right + 1 if left == 0 or right == 0 else min(left,right) + 1
        else : 
            return 0
