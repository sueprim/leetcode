class Solution:
    def countLargestGroup(self, n: int) -> int:        
        dp={0:0}      
        counts=[0]*(100)       
        for i in range(1,n+1):           
            a=i%10           
            b=i//10
            
            dp[i]  = a+dp[b]
            
            counts[dp[i]]+=1           
        return counts.count(max(counts))
