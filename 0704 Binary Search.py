class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(array,target,start,end):
            if start>end:
                return None
            mid = (start+end)//2
            if array[mid]==target:
                return mid
            elif array[mid]>target:
                return binary_search(array,target,start,mid-1)
            else:
                return binary_search(array,target,mid+1,end)
        result = binary_search(nums,target,0,len(nums)-1)
        if result==None:
            return -1
        else:
            return result
