class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root.val]

        for node in root.children:
            stack.extend(self.preorder(node))
        
        return stack
