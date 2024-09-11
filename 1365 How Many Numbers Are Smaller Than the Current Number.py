class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        b=[]
        for i in range(len(nums)):
            b.append(nums[i])
        nums.sort()
        arr=[]
        
        for i,value in enumerate(b):
            arr.append(nums.index(value))
        return arr
