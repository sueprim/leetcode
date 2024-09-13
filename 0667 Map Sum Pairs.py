class MapSum:

    def __init__(self):
        self.dic = {}

    def insert(self, key: str, val: int) -> None:
            self.dic[key] = val

    def sum(self, prefix: str) -> int:
        res = 0 
        for word in self.dic : 
            idx = word.find(prefix)
            if idx == 0 :
                res += self.dic[word]
        return res 
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
