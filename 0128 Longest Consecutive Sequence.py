class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        longest = 0

        length = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            if nums[i] + 1 == nums[i + 1]:
                length += 1
            else:
                longest = max(length, longest)
                length = 1

        longest = max(length, longest)
        return longest
