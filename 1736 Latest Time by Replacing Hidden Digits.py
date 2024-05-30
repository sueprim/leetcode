class Solution:
    def maximumTime(self, time: str) -> str:
        res = ""
        for i in range(len(time)):
            if time[i] == "?":
                if i == 0 :
                    if time[1] == "?" or time[1] <"4":
                        res +="2"
                    else : 
                        res +="1"
                elif i == 1 :
                    if res[0] == "2":
                        res += "3"
                    else :
                        res += "9"
                elif i == 3 :
                    res += "5"
                elif i == 4 :
                    res += "9"
                     
            else:
                res += time[i]
        return res
