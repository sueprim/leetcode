class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s= [x for x in s]
        a=[0]*len(s)
        for i,v in enumerate(indices):
            a[v]=s[i]
        return "".join(a)
