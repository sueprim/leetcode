class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        accumulation = {0:1}
        cnt = 0
        currentSum = 0 

        for i,n in enumerate(nums): 
            currentSum += n
            
            cnt += accumulation.get(currentSum-k, 0)
            
            accumulation[currentSum] = accumulation.get(currentSum,0) + 1
            
        return cnt
