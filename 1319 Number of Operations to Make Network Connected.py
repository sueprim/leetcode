from typing import List


class Solution:
    def __init__(self):
        self.parent = []

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        self.parent = [i for i in range(n)]
        connections_cnt = len(connections)
        for node_x, node_y in connections:
            self.merge(node_x, node_y)

        print(self.parent)
        for node in range(n):
            self.find(node)

        parent_set = set(self.parent)
        for p in parent_set:
            cnt = self.parent.count(p)
            connections_cnt -= cnt - 1

        if connections_cnt >= len(parent_set) - 1:
            return len(parent_set) - 1
        else:
            return -1

    def find(self, node: int) -> int:
        if self.parent[node] == node:
            return node

        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def merge(self, node_x: int, node_y: int):
        node_x = self.find(node_x)
        node_y = self.find(node_y)

        if node_x == node_y:
            return

        self.parent[node_x] = node_y
