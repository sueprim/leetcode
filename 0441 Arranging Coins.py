class Solution(object):
    def arrangeCoins(self, n):
        # binary search solution
        left, right = 0, n
        while left <= right:
            k = (right+left) // 2
            curr = k* (k+1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k-1
            else:
                left = k+1
        return right
