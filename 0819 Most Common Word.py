class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub('[^\w]',' ',paragraph).lower().split( ) if word not in banned]
        word_dict = {}
        most_common = collections.Counter(words).most_common(1)
        return most_common [0][0]
