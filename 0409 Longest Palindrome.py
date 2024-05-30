class Solution:
    def longestPalindrome(self, s: str) -> int:
        answer = 0
        alpha = {}
        for c in s:
            if c not in alpha:
                alpha[c] = 1
            else:
                alpha[c] += 1

        odd_exist = False
        max_odd = 0
        for value in  alpha.values():
            if value % 2 == 0:
                answer += value
            else:
                max_odd = max(max_odd,value)
                odd_exist = True
                answer += ( value -1 )
        if odd_exist:
            answer += 1
        return answer
