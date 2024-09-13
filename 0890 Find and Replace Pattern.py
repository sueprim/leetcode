class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res =[]
        
        def match(word,pattern):
            if len(word) != len(pattern):
                return False
            dir ={}
            for w,p in zip(word,pattern) :
                if w not in dir :
                    if p in dir.values():
                        return False
                    dir[w]= p
                else : 
                    if dir[w] != p :
                        return False
            return True
            
        for w in words : 
            if match(w,pattern) : 
                res.append(w)
        return res
