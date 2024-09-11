class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        x=0
        for i in range(len(sentences)):
            x=max(len(sentences[i].split()),x)
            
        return x
