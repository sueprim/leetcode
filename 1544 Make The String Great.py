class Solution:
    def makeGood(self, s: str) -> str:
        dq = deque()
        for i in range(len(s)):
            if not dq : 
                dq.append(s[i])
                continue
            if dq[-1].isupper() and ord(dq[-1]) + 32 == ord(s[i]) : 
                dq.pop()
            elif dq[-1].islower() and ord(dq[-1]) - 32  == ord(s[i]):
                dq.pop()
            else : 
                dq.append(s[i])
        return ''.join(dq)
