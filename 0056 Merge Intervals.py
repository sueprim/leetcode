class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        visited = set()
        for i in range(len(intervals)):
            if i in visited:
                continue
            visited.add(i)

            while True:
                has_merged = False
                for j in range(len(intervals)):
                    if j in visited:
                        continue
                    if (
                        intervals[i][0] <= intervals[j][1]
                        and intervals[j][0] <= intervals[i][1]
                    ):
                        visited.add(j)
                        intervals[i] = [
                            min(intervals[i][0], intervals[j][0]),
                            max(intervals[i][1], intervals[j][1]),
                        ]
                        has_merged = True
                if not has_merged:
                    break

            output.append(intervals[i])
        return output
