class Trie:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        pointer = self.tree
        for char in word:
            if char in pointer:
                pointer = pointer[char]
            else:
                pointer[char] = {}
                pointer = pointer[char]
        pointer['*'] = '*'

    def search(self, word: str) -> bool:
        pointer = self.tree
        for char in word:
            if char in pointer:
                pointer = pointer[char]
            else:
                return False
        return '*' in pointer

    def startsWith(self, prefix: str) -> bool:
        pointer = self.tree
        for char in prefix:
            if char in pointer:
                pointer = pointer[char]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)