class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        mySet = set(dictionary)
        ans = []
        for s in sentence.split(" "):
            n = len(s)
            add = False
            for i in range(1,n):
                if s[:i] in mySet:
                    ans.append(s[:i])
                    add = True
                    break
            if not add:
                ans.append(s)
        return ' '.join(ans)