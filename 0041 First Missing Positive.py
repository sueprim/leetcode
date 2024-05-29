class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numSet = set(nums)
        for num in range(1, len(nums) + 1):
            if num not in numSet:
                return num
        return len(nums) + 1
