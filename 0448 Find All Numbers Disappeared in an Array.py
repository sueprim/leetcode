class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if len(nums) < 0: 
            answer = [] 
        else: 
            max_num = len(nums)
            answer = list(set(range(1,max_num + 1)) - set(nums)) 
        return answer
