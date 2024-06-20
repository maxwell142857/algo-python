class Node:
    def __init__(self,value):
        self.val = value
        self.sons = {}
        self.shortID = None

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        # build tree with dict
        # trie = {}
        # for i in len(wordsContainer):
        #     word = wordsContainer[i][::-1]
        #     p = trie
        #     for c in word:
        #         if c not in p:
        #             p[c] = {}
        #         p = p[c]
        #     if '*' not in p:
        #         p['*']  = i

        # build tree with node
        root = Node(1)

        for i in range(len(wordsContainer)):
            word = wordsContainer[i][::-1]
            p = root
            for c in word:
                if p.shortID is None:
                    p.shortID = i
                elif len(wordsContainer[p.shortID])>len(word):
                    p.shortID = i

                if c not in p.sons:
                    p.sons[c] = Node(c)
                p = p.sons[c]

            if p.shortID is None:
                    p.shortID = i
            elif len(wordsContainer[p.shortID])>len(word):
                    p.shortID = i
        
        ans = []

                

        for word in wordsQuery:
            query = word[::-1]
            p = root
            answered = False
            for c in query:
                if c not in p.sons:
                    ans.append(p.shortID)
                    answered = True
                    break
                else:
                    p = p.sons[c]
            if not answered:
                ans.append(p.shortID)
        return ans
