class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        x=0
        for i in range(len(accounts)):
            x=max(x, sum(accounts[i]))
        return x
