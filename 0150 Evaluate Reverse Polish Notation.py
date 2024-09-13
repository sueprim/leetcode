class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st =deque()
        
        for i in range(len(tokens)):
            token = tokens[i]

            if token[0] == "-" and len(token) >1 :
                minus = int(token[1:])
                minus = -minus
                st.append(minus)
            elif token.isdigit() : 
                st.append(int(token))
            else : 
                second = st.pop()
                first = st.pop()
                if token == "+" : 
                    st.append(first+second)
                elif token == "-":
                    st.append(first-second)
                elif token == "*" : 
                    st.append(first*second)
                else : 
                    if (first < 0 and second > 0) or (first > 0 and second <0):
                        res = abs(first) // abs(second)
                        st.append(-res)
                    else : 
                        st.append(first//second)
        return st[0]
