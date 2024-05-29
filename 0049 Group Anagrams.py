class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sorted_list = str(sorted(word))
            if sorted_list not in anagrams:
                anagrams[sorted_list] = []
            anagrams[str(sorted(word))].append(word)
        return anagrams.values()
