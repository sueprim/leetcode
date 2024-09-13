class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:

        target = ord(target)
        for letter in letters:
            if target < ord(letter):
                return letter
        return letters[0]

s = Solution()
print(s.nextGreatestLetter(["c", "f", "j"], 'a')) # c
print(s.nextGreatestLetter(["c", "f", "j"], 'c')) # f
print(s.nextGreatestLetter(["c", "f", "j"], 'd')) # f
print(s.nextGreatestLetter(["c", "f", "j"], 'g')) # j
print(s.nextGreatestLetter(["c", "f", "j"], 'j')) # c
print(s.nextGreatestLetter(["c", "f", "j"], 'k')) # c
