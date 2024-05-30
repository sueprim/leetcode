class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            visited.add(node)
            for adj, connected in enumerate(isConnected[node]):
                if adj not in visited and connected == 1:
                    dfs(adj)

        cnt = 0
        visited = set()
        for node in range(len(isConnected)):
            if node not in visited:
                cnt += 1
                dfs(node)

        return cnt
