class Solution(object):
    def minSubArrayLen(self, target, nums):
    
        window_start = 0
        minimum_window = len(nums)
        running_window_sum = 0 
        check = False

        for i in range(len(nums)):
            
            running_window_sum += nums[i]

            while running_window_sum >= target:
                check = True
                minimum_window = min(minimum_window, i-window_start+1)
  
                running_window_sum -= nums[window_start]     
                window_start += 1

        if check == True:
            return minimum_window
        else:
            return 0
