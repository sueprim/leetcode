class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        dic = {}
        res = ""
        for i in range(26):
            asc = chr(i+65)
            dic[i+1] = asc
        while columnNumber : 
            temp = columnNumber%26 
            if temp == 0 :
                res+="Z"
                if columnNumber == 26 : 
                    break
            else:
                res += dic[temp]
            columnNumber = (columnNumber-1)//26
        return res[::-1]
