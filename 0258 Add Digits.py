class Solution(object):
    def addDigits(self, num):
        if num < 10:
            return num
        
        while num >= 10:
            prev = 0
            while num > 0 :
                prev += num % 10
                num = num // 10
            num = prev
        
        return num
