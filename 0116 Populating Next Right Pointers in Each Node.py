"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:

            
    def connect(self, root: 'Node') -> 'Node':
        if not root :
            return None
        dq = deque()
        res = Node()
        res2 =res
        dq.append(root)
        while dq : 
            size = len(dq)
            for i in range (size) :
                node = dq.popleft()  
                if node.left : 
                    dq.append(node.left)
                if node.right : 
                    dq.append(node.right)
                res.next = Node(node.val)
                res = res.next
            if len(dq)!= 0:
                res.next= Node("#")
                res = res.next
        
        
        return res2.next
