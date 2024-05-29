class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = len(nums) - 2
        while 0 <= low and nums[low] >= nums[low + 1]:
            low -= 1

        if low > -1:
            high = len(nums) - 1
            while 0 <= high and nums[low] >= nums[high]:
                high -= 1

            nums[low], nums[high] = nums[high], nums[low]

        start, end = low + 1, len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
