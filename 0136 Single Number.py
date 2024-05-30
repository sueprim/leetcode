class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt_dict = Counter(nums) 
        items = cnt_dict.items()
        
        for key, val in items:
            if val == 1:
                answer = key
                break
                
        return answer
