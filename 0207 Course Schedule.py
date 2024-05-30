class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        traversing = set()
        finished = set()

        def can_finish(crs):
            if crs in traversing:
                return False
            if crs in finished:
                return True

            traversing.add(crs)
            for pre in graph[crs]:
                if not can_finish(pre):
                    return False
            traversing.remove(crs)
            finished.add(crs)
            return True

        for crs in graph:
            if not can_finish(crs):
                return False
        return True
