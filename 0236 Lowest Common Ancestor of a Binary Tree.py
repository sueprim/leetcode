class Solution:
    def lowestCommonAncestor(self, node, p, q):
        if not node:
            return None

        if node == p or node == q:
            return node

        left = self.lowestCommonAncestor(node.left, p, q)
        right = self.lowestCommonAncestor(node.right, p, q)

        if left and right:
            return node

        return left if left else right
