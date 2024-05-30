class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        left = start
        right =start
        while 1:
            if nums[left] == target : 
                return abs(left - start)
            elif nums[right] == target : 
                return right-start
            if left >0 : 
                left-=1
            if right+1 < len(nums):
                right+=1
