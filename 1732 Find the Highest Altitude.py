class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0 
        tmpsum = 0
        for i in range(len(gain)):
            tmpsum += gain[i]
            res = max(tmpsum,res)
        return res
