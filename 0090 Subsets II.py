class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.s = set()
        self.solution(0,nums,[])
        return self.result
    
    def solution(self, depth : int, nums : List[int], temp : List[int]):
        if depth == len(nums):
            temp.sort()
            temp = tuple(temp)
            if temp not in self.s : 
                self.result.append(list(temp))
                self.s.add(temp)
            return
        temp.append(nums[depth])
        self.solution(depth+1,nums,temp[:])
        temp.pop()
        self.solution(depth+1,nums,temp[:])
