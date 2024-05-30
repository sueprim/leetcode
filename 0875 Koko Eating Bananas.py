class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)

        while start <= end:
            mid = (start + end) // 2

            max_h = h
            for i in range(len(piles)):
                if piles[i] > 0:
                    max_h -= math.ceil(piles[i] / mid)

            is_finish = True if max_h >= 0 else False

            if is_finish:
                end = mid - 1
            else:
                start = mid + 1

        return start
