class Solution:
    def convert(self, s: str, numRows: int) -> str:
        char_list = ["" for _ in range(numRows)]
        char_list_idx = 0
        is_down = True

        if numRows == 1:
            return s

        for char in s:
            char_list[char_list_idx] += char

            if is_down:
                if char_list_idx == numRows - 1:
                    is_down = False
                    char_list_idx -= 1
                else:
                    char_list_idx += 1
            else:
                if char_list_idx == 0:
                    is_down = True
                    char_list_idx += 1
                else:
                    char_list_idx -= 1

        return "".join(char_list)
