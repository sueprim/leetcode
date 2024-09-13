class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        res = []
        for i in range(size-3):
            if i==0 or (i>0 and nums[i] !=nums[i-1]):
                for j in range(i+1,size-2):
                    if j == i+1 or (j > i+1 and nums[j] != nums[j-1]) :
                        lo,hi,ts = j+1,size-1,target-(nums[i] +nums[j])
                        while lo < hi :
                            if nums[lo] + nums[hi] == ts :
                                res.append([nums[i],nums[j],nums[lo],nums[hi]])
                                while lo <hi and nums[lo] == nums[lo+1] :
                                    lo+=1
                                while lo < hi and nums[hi] == nums[hi-1] : 
                                    hi-=1
                                lo+=1
                                hi-=1
                            elif nums[lo] + nums[hi] < ts :
                                lo+=1
                            else:
                                hi-=1
        return res
