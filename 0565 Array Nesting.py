class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0 
        def solution(idx,nums,count) -> int: 
            if nums[idx] == -1 : 
                return count - 1
            nxtidx = nums[idx]
            nums[idx] = - 1
            return solution(nxtidx,nums,count+1)
        for idx,num in enumerate(nums) : 
            count = 0
            if nums[idx] == -1 : 
                continue
            tmpcount = solution(idx,nums,count+1)
            res = max(tmpcount,res)
        return res
