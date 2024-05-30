class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        answer = 0

        for num in nums:
            answer += self.get_divisor_sum_when_divisor_cnt_4(num)

        return answer

    def get_divisor_sum_when_divisor_cnt_4(self, x: int) -> int:
        divisor_set = set()
        total_sum = 0

        for i in range(1, int(x ** (1 / 2)) + 1):
            if x % i == 0:
                divisor_set.add(i)

        if len(divisor_set) == 2:
            for i in divisor_set:
                if i * i == x:
                    return 0
                else:
                    total_sum += i
                    total_sum += x / i

        return int(total_sum)
