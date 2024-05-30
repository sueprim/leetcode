class Solution(object):
    def countSubstrings(self, s):
        answer = 0
        
        for i in range(len(s)):
            left = i
            right = i

            # odd length
            while left >=0 and right < len(s) and s[left]==s[right]:
                answer += 1
                left -= 1
                right += 1


            # even length
            left = i
            right = i + 1
            while left >=0 and right < len(s) and  s[left]==s[right]:
                answer += 1
                left -= 1
                right += 1

        return answer
