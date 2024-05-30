class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = []
        for i in range(n):
            jobs.append([startTime[i],endTime[i],profit[i]])

        jobs = sorted(jobs,key=lambda x:x[0])

        queue = []
        current, max_profit = 0,0

        for s,e,p in jobs:

            while queue and queue[0][0] <= s:
                et , temp = heapq.heappop(queue)
                current = max(current,temp)
     
            heapq.heappush(queue,(e,current+p))
            max_profit = max(max_profit,current+p)

        return max_profit
