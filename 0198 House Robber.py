class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        curr = 0
        for i in nums:
            prev, curr = curr, max(curr, prev + i)
        return curr
