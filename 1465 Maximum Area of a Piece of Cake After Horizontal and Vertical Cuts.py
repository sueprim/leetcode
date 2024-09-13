class Solution:
    def maxArea(self, h: int, w: int, ho: List[int], ve: List[int]) -> int:
        ho.append(0)
        ho.append(h)
        ve.append(0)
        ve.append(w)
        ho.sort()
        ve.sort()
        maxrow = 0
        maxcol = 0
        for i in range(1,len(ho)):
            if ho[i] - ho[i-1] > maxrow : 
                maxrow = ho[i]-ho[i-1]
        for i in range(1,len(ve)):
            if ve[i] - ve[i-1] > maxcol : 
                maxcol = ve[i] - ve[i-1]
        return (maxrow*maxcol)%(pow(10,9)+7)
