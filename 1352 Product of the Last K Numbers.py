class ProductOfNumbers:

    def __init__(self):
        self.product = deque()
        self.zerobase = -1

    def add(self, num: int) -> None:
        if num == 0 :
            self.zerobase = len(self.product) 
        if len(self.product) == 0 :
            self.product.append(num)
        else : 
            if self.product[-1] != 0 : 
                self.product.append(num * self.product[-1])
            else : 
                self.product.append(num)

    def getProduct(self, k: int) -> int:
        idx = len(self.product) - k
        #print(self.product,idx,self.zerobase)
        if idx <= self.zerobase : 
            return 0
        if idx > 0 :
            if self.product[idx-1] == 0 :
                return self.product[-1]
            else : 
                return self.product[-1] // self.product[idx-1]
        else : 
            return self.product[-1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
