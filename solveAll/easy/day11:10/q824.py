class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(' ')
        result = []
        for i in range(len(words)):
            w = words[i]
            if w[0] in 'aeiouAEIOU':
                w += 'ma'
            else:
                w = w[1:]+w[0]+'ma'
            w += 'a'*(i+1)
            result.append(w)
        return ' '.join(result)