class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]

            if start == len(s):
                memo[start] = True
                return True

            for word in wordDict:
                if s[start : start + len(word)] == word:
                    if dfs(start + len(word)):
                        memo[start] = True
                        return True

            memo[start] = False
            return False

        return dfs(0)
