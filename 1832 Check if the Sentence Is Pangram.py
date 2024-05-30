class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dic = {}
        for word in sentence:
            if word not in dic :
                 dic[word] = 1
                 if len(dic) == 26 :
                    return True
        return False
