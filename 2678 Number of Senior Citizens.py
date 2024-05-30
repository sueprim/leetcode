class Solution:
    def countSeniors(self, details: List[str]) -> int:
        out = 0
        for detail in details:
            if int(detail[-4:-2]) >60 :
                out += 1
        return out
