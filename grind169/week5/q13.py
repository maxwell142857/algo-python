class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        p = self.trie
        for c in word:
            if c in p:
                p = p[c]
            else:
                p[c] = {}
                p = p[c]
        p['*'] = {}

    def search(self, word: str) -> bool:
        def DFS(cur,index):
            if index == len(word):
                return '*' in cur
            
            c = word[index]
            if c != '.':
                if c in cur:
                    return DFS(cur[c],index+1)
                else:
                    return False
            else:
                result = False
                keys = cur.keys()
                for key in keys:
                    result |= DFS(cur[key],index+1)
                    if result:
                        return True
                return False
        
        return DFS(self.trie,0)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)