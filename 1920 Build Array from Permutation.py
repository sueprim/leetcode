class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = deque()
        for i in nums:
            res.append(nums[i])
        return res
