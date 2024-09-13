class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        idx = 0
        dominoes = list(dominoes)
        while idx < len(dominoes) :
            if dominoes[idx] == '.' :
                left = idx
                right = idx
                while left > 0 and dominoes[left] == '.' : 
                    left-=1
                while right+1 < len(dominoes) and dominoes[right] == '.' : 
                    right+=1
                if dominoes[right] == 'L' :
                    if dominoes[left] == 'R':
                        while left+1 < right-1 : 
                            dominoes[left+1] = 'R'
                            dominoes[right-1] = 'L'
                            left+=1
                            right-=1
                    else : 
                        while left < right :  
                            dominoes[left] = 'L'
                            left+=1
                else : 
                    if dominoes[left] == 'R' :
                        while left <= right : 
                            dominoes[left] = 'R'
                            left+=1 
            idx+=1
        
        return ''.join(dominoes)
