class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        firstnum = ""
        secondnum =""
        targetnum = ""
        for i in range(len(firstWord)):
            firstnum += str(ord(firstWord[i])-97)
        for i in range(len(secondWord)):
            secondnum += str(ord(secondWord[i]) - 97)
        for i in range(len(targetWord)) : 
            targetnum += str(ord(targetWord[i]) - 97)
        return int(targetnum) == (int(firstnum) + int(secondnum))
