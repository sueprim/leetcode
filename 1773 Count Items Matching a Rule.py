class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0 
        idx = -1
        if ruleKey == "type" : 
            idx = 0
        elif ruleKey == "color":
            idx = 1
        else : 
            idx = 2
        for i in range(len(items)):
            if items[i][idx] == ruleValue : 
                res+=1
        return res
