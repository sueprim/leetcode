class Solution:
    result_price = 0

    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        dp = {}
        for i in range(len(price)):
            self.result_price += price[i] * needs[i]

        def dfs(need, cost, s):

            for i in range(s, len(special)):
                flag = True
                row_cost = 0
                current_need = need[:]
                for j in range(len(current_need)):
                    if current_need[j] < special[i][j]:
                        flag = False
                        break
                    current_need[j] -= special[i][j]
                    row_cost += current_need[j] * price[j]

                if flag:
                    current_cost = special[i][-1] + cost + row_cost
                    key = str(current_need)
                    if dp.get(key) and dp.get(key) <= current_cost:
                        continue
                    self.result_price = min(self.result_price, current_cost)
                    dp[key] = current_cost
                    dfs(current_need, cost + special[i][-1], i)

        dfs(needs, 0, 0)
        return self.result_price
