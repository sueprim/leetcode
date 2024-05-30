class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        num = left
        for i in range(len(ranges)) : 
            while num <=right and ranges[i][0] <= num and num <= ranges[i][1] :
                num+=1
            if num > right:
                return True
        return False
