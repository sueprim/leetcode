class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        res ={}
        maxnum = 0 
        for i in range(len(rectangles)):
            temp = min(rectangles[i][0],rectangles[i][1])
            maxnum = max(maxnum,temp)
            if temp not in res :
                res[temp] = 1
            else :
                res[temp] += 1
        return res[maxnum]
