class Solution:
    def sortSentence(self, s: str) -> str:
        stsp = s.split(" ")
        resli = [""] * len(stsp)
        res = ""
        for i in range(len(stsp)):    
            resli[int(stsp[i][-1])-1] = stsp[i][:-1]
        for i in range(len(resli)):
            res += resli[i] + " "
        return res[:-1]
