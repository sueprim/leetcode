class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        
        for i, row in enumerate(mat):
            strength = row.count(1)
            heappush(heap, (strength, i))

        res = []
        for _ in range(k):
            strength, idx = heappop(heap)
            res.append(idx)

        return res
