class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result, nums = [], []

        def dfs(start, total):
            if total > target:
                return
            if total == target:
                return result.append(nums[:])
            for i in range(start, len(candidates)):
                num = candidates[i]
                nums.append(num)
                dfs(i, total + num)
                nums.pop()

        dfs(0, 0)
        return result
