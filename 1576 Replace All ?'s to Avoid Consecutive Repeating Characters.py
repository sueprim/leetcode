import random
class Solution:
    def modifyString(self, s: str) -> str:
        res = ""
        left = 0 
        right = 0
        for i in range(len(s)):
            if s[i] == "?" : 
                if i!= 0 : 
                    left = ord(res[i-1])
                if i!= len(s)-1 :
                    right = ord(s[i+1])
                rand = random.randrange(97,122)
                while rand == left or rand == right :
                    rand = random.randrange(97,122)
                res += chr(rand)
            else : res += s[i]
        return res
