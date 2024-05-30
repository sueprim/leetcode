class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        answer = False

        if len(s) != len(t):
            return answer
        
        else:
            s_check = []
            t_check = []
            for i in s:
                s_check.append(s.index(i))

            for j in t:
                t_check.append(t.index(j))

            if s_check == t_check:
                answer = True
            
            return answer
