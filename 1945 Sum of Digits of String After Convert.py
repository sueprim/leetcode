class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = 0
        convert = ""
        loop = 0
        while loop <= k :
            if loop == 0 :
                for i in range(len(s)):
                    convert += str((ord(s[i]) - 96))
            else : 
                res = 0 
                for i in range(len(s)):
                    res += int(s[i])
                convert = str(res)
            loop+=1
            s = convert
            convert = ""
        return res
