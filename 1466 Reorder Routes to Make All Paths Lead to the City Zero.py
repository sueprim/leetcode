from collections import deque
from typing import List


class Solution:
    def __init__(self):
        self.answer = 0

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        connection_list = [[] for _ in range(n)]

        for connection in connections:
            start, end = connection
            connection_list[start].append([end, True])
            connection_list[end].append([start, False])

        self.bfs(n, connection_list)

        return self.answer

    def bfs(self, n: int, connection_dic):
        visit = [False for _ in range(n)]
        visit[0] = True
        q = deque()

        for connection in connection_dic[0]:
            q.append(connection)

        while len(q) > 0:
            destination, is_direction = q.popleft()

            if not visit[destination]:
                visit[destination] = True
                if is_direction:
                    self.answer += 1
                for connection in connection_dic[destination]:
                    q.append(connection)
