class Solution:
    def myAtoi(self, s: str) -> int:
        PLUS = "+"
        MINUS = "-"
        MAX_INT = (2 ** 31) - 1
        MIN_INT = -2 ** 31

        answer = ""
        s = s.lstrip()

        if s and s[0] == MINUS:
            answer += MINUS
            s = s[1:]
        elif s and s[0] == PLUS:
            s = s[1:]

        for target in s:
            if target.isdigit():
                answer += target
            else:
                break
        print(answer)
        if not answer or answer == MINUS:
            return 0

        int_answer = int(answer)

        if int_answer > MAX_INT:
            int_answer = MAX_INT
        elif int_answer < MIN_INT:
            int_answer = MIN_INT

        return int_answer
