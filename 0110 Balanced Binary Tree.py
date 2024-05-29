# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkdepth(self,root : TreeNode) -> int:
        if root : 
            left = self.checkdepth(root.left)
            if left == -1 :
                return -1
            right = self.checkdepth(root.right)
            if right == -1 :
                return -1
            if abs(left-right) > 1 :
                return -1
            return max(left,right) +1
        else : 
            return 0
        return count
    def isBalanced(self, root: TreeNode) -> bool:
        res = self.checkdepth(root)
        return False if res == -1 else True
