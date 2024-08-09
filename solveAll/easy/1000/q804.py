class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        convert = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = set()
        for w in words:
            cur = ''
            for c in w:
                cur += convert[ord(c)-ord('a')]
            result.add(cur)
        return len(result)