class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        chrli = [0] * 26
        maxnum = 0
        size = len(words)
        if size == 1 : 
            return True
        for i in range(size):
            for j in range(len(words[i])):
                chrli[ord(words[i][j]) - 97]+=1
        for i in range(len(chrli)):
            if chrli[i] != 0 and chrli[i] % size !=0  : 
                return False
        return True
