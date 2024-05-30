# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans =[]

        def foo(cur):
            if cur.left is not None: foo(cur.left)
            ans.append(cur.val)
            if cur.right is not None: foo(cur.right)
        
        if root is not None:
            foo(root)
        
        return ans
