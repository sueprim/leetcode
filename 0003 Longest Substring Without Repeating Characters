class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        # key = char / value = index
        char_dic = {}
        left_idx = 0

        for right_idx, char in enumerate(s):
            if char not in char_dic:
                answer = max(answer, (right_idx - left_idx + 1))
            else:
                if char_dic[char] < left_idx:
                    answer = max(answer, (right_idx - left_idx + 1))
                else:
                    left_idx = char_dic[char] + 1

            char_dic[char] = right_idx

        return answer
