class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0 
        for i in range(len(arr)):
            window = 0
            while i + window < len(arr) : 
                res += sum(arr[i:i+window+1])
                window+=2
        return res
