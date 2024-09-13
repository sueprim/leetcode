class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic : 
                dic[nums[i]]=1
            else : 
                dic[nums[i]]+=1
                if dic[nums[i]] == 3 :
                    del[dic[nums[i]]]
        res = list(dic.keys())
        return res[0]
