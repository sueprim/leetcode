class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollar = 0
        ten_dollar = 0
        result = True
        
        if bills[0] == 10:
            result = False
        
        for i in range(len(bills)):
            if bills[i] == 5:
                five_dollar +=1
                result = True
            elif bills[i] == 10:
                if five_dollar >= 1:
                    ten_dollar +=1
                    five_dollar -=1
                    result = True
                else:
                    result = False
                    break
            elif bills[i] == 20:
                if ten_dollar >= 1 and five_dollar >= 1:
                    ten_dollar -=1
                    five_dollar -=1
                    result = True
                elif ten_dollar == 0 and five_dollar >= 3:
                    five_dollar -=3
                    result = True
                else:
                    result = False
                    break
                    
        return result
