class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = {}
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = True
        
    def search(self, word: str) -> bool: 
        """
        Returns if the word is in the trie.
        """
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        if '*' in cur:
            return True
        return False
        
    def startsWith(self, prefix: str) -> bool: 
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.head
        for ch in prefix:
            if ch not in cur:
                return False
            cur = cur[ch]
        return True
