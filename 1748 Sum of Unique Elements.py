class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        res = [0] * 101
        ans = 0
        for i in range(len(nums)):
            res[nums[i]] +=1
        for i in range(len(res)):
            if res[i]== 1 :
                ans+=i
        return ans
