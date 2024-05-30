class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        res = ""
        for i in range(len(n)-1, -1,-1) :
            if (len(n)- i - 1) %3 == 0 :
                    res+= "."
            res+=n[i]
        return res[::-1][:-1]
