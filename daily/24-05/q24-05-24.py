from collections import Counter,defaultdict
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        storage = Counter(letters)
        used = defaultdict(int)
        
        def check(s):
            need = Counter(s)
            for key,val in need.items():
                if key not in storage or storage[key]<used[key]+val:
                    return False
            return True
        
        def update(s,sign):
            need = Counter(s)
            for key,val in need.items():
                used[key] += sign*val

        def calculateScore():
            tmp = 0
            for k,v in used.items():
                tmp += score[ord(k)-ord('a')]*v
            return tmp
        
        ans = 0
        def backTracking(index):
            nonlocal ans
            if index == n:
                ans = max(ans,calculateScore())
                return
            
            # do not use current word
            backTracking(index+1)

            # use current word
            if check(words[index]):
                update(words[index],1)
                backTracking(index+1)
                update(words[index],-1)
        
        backTracking(0)
        return ans

