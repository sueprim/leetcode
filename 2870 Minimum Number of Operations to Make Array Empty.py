class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 2:
            if nums[0] != nums[1]:
                return -1
            else:
                return 1

        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        answer = 0
        for count in counts.values():
            if count == 1:
                return -1
            if count % 3 == 0:
                answer += (count // 3)
            else:
                answer += (count // 3) + 1

        return answer
