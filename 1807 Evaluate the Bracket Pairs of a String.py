class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        #list to dic
        dic = {}
        for i in range(len(knowledge)):
            dic[knowledge[i][0]] = knowledge[i][1]
        #임시로 문자열을 담을 변수
        temp = ""
        #결과 문자열
        res = ""
        i = 0
        sz = len(s)
        while i < sz:
            if s[i] =="(" : 
                i+=1
                while i< sz and s[i] != ")":
                    temp += s[i]
                    i+=1
                if temp in dic : 
                    res+= dic[temp]
                else : 
                    res += "?"
            else : 
                res += s[i]
            temp = ""
            i+=1
        return res   
