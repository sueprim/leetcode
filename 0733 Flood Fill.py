from collections import deque


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        old = image[sr][sc]

        image[sr][sc] = color
        queue = deque([(sr, sc)])

        while queue:
            row, col = queue.popleft()
            for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= row + r < len(image) and 0 <= col + c < len(image[0]):
                    if image[row + r][col + c] == old:
                        image[row + r][col + c] = color
                        queue.append((row + r, col + c))
        return image
