class Solution:
    def findScore(self, nums: List[int]) -> int:

        res = 0
        tmp = [(num,idx) for idx,num in enumerate(nums)]
        heapq.heapify(tmp)

        marked = set()
        
        while tmp:
            num, idx = heapq.heappop(tmp)
            if idx not in marked:
                res += num
                marked.add(idx)
                marked.add(idx-1)
                marked.add(idx+1)

        return res
