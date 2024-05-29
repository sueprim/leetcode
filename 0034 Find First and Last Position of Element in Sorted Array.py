class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                low, high = mid, mid
                while 0 <= low - 1 and nums[low - 1] == target:
                    low -= 1
                while high + 1 < len(nums) and nums[high + 1] == target:
                    high += 1
                return [low, high]
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return [-1, -1]
