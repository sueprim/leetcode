class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        idx1 = num1.index('+')
        idx2 = num2.index('+')
        real1 = num1[:idx1]
        real2 = num2[:idx2]
        imag1 = num1[idx1+1:num1.find('i')]
        imag2 = num2[idx2+1:num2.find('i')]
        num1 = complex(int(real1),int(imag1))
        num2 = complex(int(real2),int(imag2))
        res = num1 * num2
        temp = ""
        if res.real == 0 :
            temp += "0+"
        else : 
            temp += str(res.real)[:-2] + "+"
        temp += str(res.imag)[:-2] + "i"
        return temp
