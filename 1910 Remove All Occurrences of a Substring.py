class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        size = len(part)
        while True : 
            idx = s.find(part)
            if idx == -1 : 
                break
            else : 
                s = s[:idx] + s[idx + size:]
        return s
