class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lifetime = [0] * 1001
        for i in range(len(trips)):
            lifetime[trips[i][1]] += trips[i][0]
            lifetime[trips[i][2]] -= trips[i][0]
        for i in range(1001):
            if capacity < 0 :
                return False
            capacity -= lifetime[i]
                    
        return True
