class Solution:
    def isHappy(self, n: int) -> bool:
        nSet = set()

        while n not in nSet:
            nSet.add(n)
            n = self.sumOfSquares(n)
            if n ==1 :
                return True       
        return False

    
    def sumOfSquares(self, n:int) -> int:
        output = 0

        while n:
            digit = n%10
            digit = digit **2
            output += digit
            n = n //10
        return output
