from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = 0
        rotations = -1

        current_profit = 0
        wait = 0

        rotates = 0

        while wait or rotates < len(customers):
            if rotates < len(customers):
                wait += customers[rotates]
            rotates += 1
            boarding = min(wait, 4)
            wait -= boarding

            current_profit += boarding * boardingCost - runningCost

            if max_profit < current_profit:
                max_profit = current_profit
                rotations = rotates

        return rotations
