class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for char in s:
            d[char] = d.get(char, .0) + 1
        return len(set(d.values())) == 1
