class Solution:
    def secondHighest(self, s: str) -> int:
        check = [0] * 10
        for i in range(len(s)):
            if s[i].isdigit():
                check[ord(s[i]) -48] +=1
        first = False
        for i in range(len(check)-1,-1,-1):
            if check[i] != 0 :
                if first == False : 
                    first = True
                else : 
                    return i
        return -1
