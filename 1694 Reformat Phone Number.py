class Solution:
    def reformatNumber(self, number: str) -> str:
        #brute list
        sz = len(number)
        resli = deque()
        count = 0 
        for i in range(sz):
            if number[i].isdigit():
                count+=1
                resli.append(number[i])
                if count%3 == 0 :
                    resli.append("-")
        if count%3 == 0 :
            resli.pop()
        if count%3 == 1 : 
            resli[-3],resli[-2] = resli[-2], resli[-3]
        return ''.join(resli)
