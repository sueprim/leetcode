class Solution:
    def customSortString(self, order: str, str: str) -> str:
        counting = 0 
        res = ""
        dic = {}
        for word in (order):
            res += str.count(word) * word
            dic[word] = 1
        for word in str : 
            if word in dic : 
                continue
            else : 
                res += word
        print(res)
        return res
