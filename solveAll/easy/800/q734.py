class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        word2word = defaultdict(set)
        for w1,w2 in similarPairs:
                
            word2word[w1].add(w2)
            word2word[w2].add(w1)

        if len(sentence1) != len(sentence2):
            return False
        
        for i in range(len(sentence1)):
            w1 = sentence1[i]
            w2 = sentence2[i]
            if (w1 in word2word and w2 in word2word[w1]) or w1==w2:
                continue
            else:
                return False
        return True