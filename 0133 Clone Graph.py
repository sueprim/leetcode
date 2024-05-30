from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}

        def dfs(node):
            if node in clones:
                return clones[node]
            clones[node] = Node(node.val)
            clones[node].neighbors = [dfs(nei) for nei in node.neighbors]
            return clones[node]

        return dfs(node) if node else None
