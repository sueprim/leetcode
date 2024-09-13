class StockSpanner:

    def __init__(self):
        self.dq = deque()

    def next(self, price: int) -> int:
        res = 1
        while self.dq and self.dq[-1][0] <= price : 
            res += self.dq.pop()[1]
        self.dq.append((price,res))
        return res
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
