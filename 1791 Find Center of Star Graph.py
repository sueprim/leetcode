class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dic ={}
        n  = len(edges)
        for i in range(len(edges)):
            first,second = edges[i]
            if first not in dic : 
                dic[first] = 1
            else : 
                dic[first] += 1
            if second not in dic :
                 dic[second] = 1
            else : 
                dic[second] += 1
        for i in dic :
            if dic[i] == n : 
                return i
