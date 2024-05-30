class Solution(object):
    def countNicePairs(self, nums):
     
        mod = 10 ** 9 + 7
        rev_nums = []

        for n in nums:
            rev_nums.append(int(str(n)[::-1]))
            
        diff = []
        for i in range(len(nums)):
            a = nums[i] - rev_nums[i]
            diff.append(a)
        
        frq_count = Counter(diff)
        count = list(frq_count.values())
  
        total = 0
        for c in count:
            total += (c*(c-1)) //2
        
        return total % mod
