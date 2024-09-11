class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        a=[]
        i=0
        while i<len(nums):
            a+=[nums[i+1]]*nums[i]
            i+=2
        return a
