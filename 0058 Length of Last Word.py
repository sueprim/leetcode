class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.split(' ')
        for i in range(len(lst) - 1 , -1, -1):
            if len(lst[i]) != 0:
                return (len(lst[i]))
        return 0
