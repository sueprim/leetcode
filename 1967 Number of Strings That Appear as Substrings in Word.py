class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        out = 0
        for pattern in patterns:
            if pattern in word:
                out += 1
        return out
