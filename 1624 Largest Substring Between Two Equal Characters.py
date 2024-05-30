class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dic = {}
        ans = -1
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
            else : 
                ans = max(ans,i - dic[s[i]] - 1) 
        return ans
