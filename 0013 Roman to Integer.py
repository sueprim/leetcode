class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        dic = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        for i in range(len(s)-1):
            if dic[s[i]] < dic[s[i+1]]:
                answer -= dic[s[i]]
            else:
                answer += dic[s[i]]
        return answer+dic[s[-1]]
