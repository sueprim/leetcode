class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0 
        for i in range(len(s) - 2) :
            temp = s[i:i+3]
            st = set()
            for j in range(3) : 
                if temp[j] in st : 
                    break
                st.add(temp[j])
                if j == 2 :
                    ans+=1
        return ans
