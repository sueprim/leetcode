class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        DP = [0] * len(nums)
        res = nums[0]
        DP[0] = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i] : 
                DP[i] = DP[i-1] + nums[i]
            else : 
                DP[i] = nums[i]
            res = max(res,DP[i])
        return res
