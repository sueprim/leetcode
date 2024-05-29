# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return None
        
        queue = deque([root])
        answer = []

        while queue:
            level = []
            length = len(queue)
            for _ in range(length):
                now = queue.popleft()
                level.append(now.val)
                if now.left:
                    queue.append(now.left)
                if now.right:
                    queue.append(now.right)
            answer.append(level)
        
        return answer
