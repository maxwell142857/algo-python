import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+',paragraph.lower())
        w2cnt = Counter(words)
        array = [(-cnt,w) for w,cnt in w2cnt.items()]
        array.sort()
        p = 0
        banned = set(banned)
        while array[p][1] in banned:
            p += 1
        return array[p][1]
       