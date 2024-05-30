from typing import List


class Solution:

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        dp = {}
        s = set(arr)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[j] - arr[i] < arr[i] and arr[j] - arr[i] in s:
                    dp[arr[i], arr[j]] = dp.get((arr[j] - arr[i], arr[i]), 2) + 1

        return max(dp.values() or [0])
