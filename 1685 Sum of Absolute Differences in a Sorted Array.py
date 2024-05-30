class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
   
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]

        for idx in range(1,n):
            prefix[idx] = prefix[idx-1] + nums[idx]
        # print(prefix)

        suffix = [0] * n
        suffix[-1] = nums[n-1]

        for idx in range(n-2,-1,-1):
            suffix[idx] = suffix[idx+1] + nums[idx] 
        # print(suffix)
        
        answer = [0] * n
        answer[0] = suffix[1] - nums[0] * (n-1)
        answer[-1] = (n-1) * nums[-1] - prefix[-2]

        for idx in range(1,n-1):

            left = (nums[idx] * idx) - prefix[idx-1]
            right = suffix[idx+1] - (nums[idx] * (n-idx-1))
            
            answer[idx] = left + right
        

        return answer
