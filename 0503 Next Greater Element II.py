class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = deque()
        sz = len(nums)
        res = [-1] * sz
        for i in range(sz * 2): 
            while stack and nums[stack[-1]] < nums[i%sz] : 
                res[stack.pop()] = nums[i % sz]
            stack.append(i%sz)
        return res
