class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = ""
        st  = deque()
        for i in range(len(s)):
            if st :
                if st[-1] == s[i] : 
                    st.pop()
                else : 
                    st.append(s[i])
            else : 
                st.append(s[i])
        while st : 
            res+=st.popleft()
        return res
