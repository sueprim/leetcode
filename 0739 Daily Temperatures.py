class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        lst= [0]*len(temperatures)
        for key, val in enumerate(temperatures):
            while stack and val > temperatures[stack[-1]]:
                last = stack.pop()
                lst[last] = key - last 
            stack.append(key)
        return lst
