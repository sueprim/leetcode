class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        #Hardcoding
        countinglist = [0] * 150
        for i in range(len(logs)):
            for j in range(logs[i][0], logs[i][1]):
                countinglist[j-1950] +=1
        return countinglist.index(max(countinglist)) + 1950
