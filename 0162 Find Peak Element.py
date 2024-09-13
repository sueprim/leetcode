class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def binary(left,right,nums):
            if left == right : 
                return left
            mid = (left + right) //2
            mid2 = mid+1
            if nums[mid] > nums[mid2] :
                return binary(left,mid,nums)
            else : 
                return binary(mid2,right,nums)
                
            
        return binary(0,len(nums)-1,nums)
