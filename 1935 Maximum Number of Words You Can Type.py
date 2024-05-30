class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        chrlist = [0] * 26
        for i in range(len(brokenLetters)) :
            chrlist[ord(brokenLetters[i])-97] = 1
        res = 0
        for word in text:
            check = False
            for j in range(len(word)):
                if chrlist[ord(word[j])-97] == 1:
                    check = True
                    break
            if not check: 
                res+=1
                
        return res
