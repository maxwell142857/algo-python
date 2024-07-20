from collections import defaultdict,Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        repo = defaultdict(int)
        licensePlate = licensePlate.lower()
        for c in licensePlate:
            if 'a'<=c<='z':
                repo[c] += 1
        
        def checkCompleting(word):
            count = Counter(word)
            for k,v in repo.items():
                if k not in count or count[k]<v:
                    return False
            return True
        ans = None
        for w in words:
            if checkCompleting(w):
                if not ans or len(ans) > len(w):
                    ans = w
        return ans
