class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = [1] * len(nums)
        for i in range(len(nums) - 1):
            before[i + 1] = before[i] * nums[i]

        after = [1] * len(nums)
        for i in range(len(nums) - 1, 0, -1):
            after[i - 1] = after[i] * nums[i]

        products = []
        for l, r in zip(before, after):
            products.append(l * r)

        return products
