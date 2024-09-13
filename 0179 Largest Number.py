class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            return str(a) + str(b) > str(b) + str(a)

        iters = len(nums) - 1
        for i in range(iters):
            wall = iters - i
            for j in range(wall):
                if not compare(nums[j], nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return str(int(''.join(map(str, nums))))
