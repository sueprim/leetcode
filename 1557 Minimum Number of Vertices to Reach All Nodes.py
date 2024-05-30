class Solution:

    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        reachable = set()
        for edge in edges:
            reachable.add(edge[1])

        not_reachable= []
        for i in range(n):
            if i not in reachable:
                not_reachable.append(i)

        return not_reachable
