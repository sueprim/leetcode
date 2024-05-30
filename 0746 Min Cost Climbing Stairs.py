class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        res = [0] * (len(cost))
        res[0] = cost[0]
        res[1] = cost[1]
        for i in range(2,len(cost)):
            res[i] = min(res[i-2] + cost[i], res[i-1] + cost[i])
        return res[len(res)-1]
