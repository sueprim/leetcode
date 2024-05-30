from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = []
        cnt = Counter(nums).most_common(k)
        for i in range(k):
            ret.append(cnt[i][0])
        return ret
