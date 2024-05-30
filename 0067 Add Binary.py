class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a)-1
        j = len(b)-1
        carry = 0
        num = 0
        res = ""
        while i >=0 and j >=0 :
            sum = int(a[i]) + int(b[j]) + carry
            carry = int(sum) //2
            num = int(sum)%2
            res +=str(num)
            i-=1
            j-=1
        while i>=0 : 
            sum = int(a[i]) + carry
            carry = int(sum) //2
            num = int(sum)%2
            res +=str(num)
            i-=1
        while j>=0:
            sum = int(b[j]) + carry
            carry = int(sum) //2
            num = int(sum)%2
            res +=str(num)
            j-=1
        if carry ==1:
            res+="1"
        return res[::-1]
