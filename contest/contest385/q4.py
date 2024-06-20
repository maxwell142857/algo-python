from collections import defaultdict
from typing import List


class dictTree:
    def __init__(self) -> None:
        self.root = {}

    def addword(self,word,isReversed = False):
        pointer = self.root
        possibleWords = []
        for char in word:
            if char not in pointer:
                pointer[char] = {}
            pointer = pointer[char]
            if '#' in pointer:
                if not isReversed:
                    possibleWords.append(pointer['#'])
                else:
                    possibleWords.append(pointer['#'][::-1])
                
        pointer['#'] = word
        return possibleWords

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        tree = dictTree()
        reverseTree = dictTree()
        word2cnt = defaultdict(int)
        ans = 0
        for i in range(len(words)):
            candidate1 = set(tree.addword(words[i]))
            candidate2 = reverseTree.addword(words[i][::-1],True)
            for c in candidate2:
                if c in candidate1:
                    ans += word2cnt[c]
            
            word2cnt[words[i]] += 1

        return ans