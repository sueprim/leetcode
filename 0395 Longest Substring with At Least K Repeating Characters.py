class Solution:
    def longestSubstring(self, s: str, k: int) -> int:      
        if len(s) == 0 or k > len(s) :
            return 0
        if k ==0 :
            return len(s)
        
        #기존 코드 효율성 있게 바꾸기.
        '''
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic : 
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        idx = 0
        while idx < len(s) and dic[s[idx]] >=k :
            idx+=1
        '''
        idx = 0
        while idx < len(s) and s.count(s[idx]) >=k :
            idx+=1
        if idx == len(s):
            return len(s)
        left = self.longestSubstring(s[:idx],k)
        right = self.longestSubstring(s[idx+1:],k)
            
        return max(left,right)
