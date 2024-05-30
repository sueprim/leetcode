class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = set()
        i = 0 
        while i < len(word) :
            temp = "" 
            while i <len(word) and word[i].isdigit() :
                temp += word[i]
                i+=1
            if temp != "" : 
                temp = int(temp)
                s.add(temp)
                temp = ""
                i-=1
            i+=1
        return len(s)
