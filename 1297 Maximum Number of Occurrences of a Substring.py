import collections


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        sub_str_dic = collections.defaultdict(int)

        start = 0
        end = start + minSize

        while len(s) >= end:
            if end - start > maxSize:
                start += 1
                continue
            elif end - start < minSize:
                end += 1
                continue

            sub_str = s[start:end]
            if self.check_duplicate_char(sub_str, maxLetters):
                sub_str_dic[sub_str] += 1

            if end - start == minSize:
                end += 1
            else:
                start += 1

        return max(sub_str_dic.values()) if sub_str_dic else 0

    def check_duplicate_char(self, sub_str: str, max_letters: int) -> bool:
        char_set = set(sub_str)

        if max_letters < len(char_set):
            return False

        return True
