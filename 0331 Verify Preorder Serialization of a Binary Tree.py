class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        tmp = preorder.split(',')
        slot = 1 
        for i in tmp : 
            if slot == 0 : 
                return False
            if i == '#' : 
                slot -= 1 
            else : 
                slot += 1
        return True if slot ==0 else False
