class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x :x[1],reverse = True)
        res = 0
        for nob,noupb in boxTypes:
            if truckSize < nob : 
                res += truckSize * noupb
                return res
            else:
                res += (noupb * nob)
                truckSize -= nob
        return res
