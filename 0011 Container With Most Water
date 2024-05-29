class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        i = 0
        j = l-1
        area = 0
        h = height
        while(i < j):
            if h[i] < h[j]:
                area = max(area, h[i] * (j -  i))
                i += 1
            else:
                area = max(area, h[j] * (j - i))
                j -= 1
        return area
