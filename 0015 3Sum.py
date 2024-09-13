class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if i> 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums)-1
            while left < right:
                lst_3 = [nums[left], nums[i], nums[right]]
                if sum(lst_3) < 0:
                    left += 1
                elif sum(lst_3) > 0:
                    right -= 1
                else:
                    lst_3.sort()
                    result.append(lst_3)
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right -1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result
