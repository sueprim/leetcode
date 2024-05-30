class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = len(nums) - (k % len(nums))
        rotated = nums[pivot:] + nums[:pivot]
        for i in range(len(nums)):
            nums[i] = rotated[i] 
