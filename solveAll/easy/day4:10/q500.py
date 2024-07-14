class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set('qwertyuiop'),set('asdfghjkl'),set('zxcvbnm')]
        
        ans = []
        for word in words:
            index = -1
            canForm = True
            for c in word:
                c = c.lower()
                for i in range(3):
                    if c in rows[i]:
                        cur = i
                if index == -1 or index == cur:
                    index = cur
                else:
                    canForm = False
                    break
            if canForm:
                ans.append(word)
        return ans
                