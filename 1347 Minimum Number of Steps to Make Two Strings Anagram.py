class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dic = {}

        result = 0

        for sub_s in s:
            s_dic[sub_s] = s_dic.get(sub_s, 0) + 1

        for sub_t in t:
            if sub_t in s_dic:
                s_dic[sub_t] -= 1

                if s_dic[sub_t] < 0:
                    result += 1

            else:
                result += 1

        return result
