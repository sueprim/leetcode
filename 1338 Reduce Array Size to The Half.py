class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dic = {}
        temp = []
        size = len(arr)
        for i in range(size):
            if arr[i] not in dic : 
                dic[arr[i]]=1
            else: 
                dic[arr[i]]+=1
        for num in dic : 
            temp.append(dic[num])
        temp.sort(reverse = True)
        res = 0 
        sumd = 0
        for i in range(len(temp)):
            if sumd < size//2 : 
                sumd += temp[i]
                res+=1
            else : 
                return res
        return 1
