class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0 : 
            return True
        if len(flowerbed) == 1 :
            if flowerbed[0]== 1 and n==1 :
                return False
            else : 
                return True
        for i in range(len(flowerbed)):
            if i == 0 and flowerbed[i] == 0:
                if flowerbed[i+1] == 0 :
                    n-=1
                    flowerbed[i]=1
            elif i == (len(flowerbed)-1)  : 
                if(flowerbed[i-1] == 0) and flowerbed[i] == 0: 
                    n-=1
                    flowerbed[i]=1
            else:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i]==0 : 
                    n-=1
                    flowerbed[i]=1
            if n<1 : 
                return True
        return False
