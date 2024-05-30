class Solution:
    def countDigits(self, num: int) -> int:
        out = 0
        for i in str(num):
            if num % int(i) == 0:
                out += 1
        return out
