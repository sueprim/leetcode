class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        pick = nums[size//2]
        res = 0 
        for i in range(size) : 
            res += abs(nums[i] - pick)
        return res
