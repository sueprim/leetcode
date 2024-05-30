class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for i in range(len(words)):
            res = 0 
            size = len(words[i])
            for j in range(len(allowed)):
                res += words[i].count(allowed[j])
            if res == size : 
                ans += 1
        return ans
