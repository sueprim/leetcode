class Solution:
    def check(self, nums: List[int]) -> bool:
        temp = nums[:]
        temp.sort()
        nums = deque(nums)
        temp = deque(temp)
        for i in range(len(nums)):
            if temp == nums:
                return True
            else:
                shift = nums.popleft()
                nums.append(shift)
            
        return False
