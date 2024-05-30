class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_table = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []
        for c in s:
            if parentheses_table.get(c) is None:
                stack.append(c)
                print(stack)

            elif not stack or parentheses_table.get(c) != stack.pop():
                return False

        return len(stack) == 0
