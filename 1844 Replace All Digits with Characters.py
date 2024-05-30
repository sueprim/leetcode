class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            if i%2 == 0 :
                temp = ord(s[i])
                res += s[i]
            else : 
                res+= chr(temp+ int(s[i]))
        return res
