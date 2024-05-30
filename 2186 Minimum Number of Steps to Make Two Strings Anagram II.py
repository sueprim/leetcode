class Solution:
    def minSteps(self, s: str, t: str) -> int:
        same_count = 0
        count_dic = defaultdict(int)

        for char in s:
            count_dic[char] += 1

        for char in t:
            if count_dic[char] and count_dic[char] > 0:
                count_dic[char] -= 1
                same_count += 1

        return len(s) - same_count + len(t) - same_count
