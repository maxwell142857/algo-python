class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        lenA = len(a)
        lenB = len(b)
        indexA = []
        indexB = []
        for i in range(n):
            if s[i:i+lenA] == a:
                indexA.append(i)
            if s[i:i+lenB] == b:
                indexB.append(i)

        # start = 0
        # while start < len(s):
        #     index = s.find(a, start)
        #     if index == -1:
        #         break
        #     indexA.append(index)
        #     start = index + 1
        # start = 0
        # while start < len(s):
        #     index = s.find(b, start)
        #     if index == -1:
        #         break
        #     indexB.append(index)
        #     start = index + 1

        ans = []
        index = 0
        for aa in indexA:
            while index < len(indexB) and abs(aa-indexB[index])>k:
                index += 1
            if index != len(indexB):
                ans.append(aa)
            else:
                index = 0
        return ans
    
