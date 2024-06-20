class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aa = list(a)
        bb = list(b)
        aa.reverse()
        bb.reverse()
        while len(aa) < len(bb):
            aa.append(0)
        while len(bb) < len(aa):
            bb.append(0)
        p = 0
        addOne = 0
        ans = []
        for p in range(len(aa)):
            result = int(aa[p])+int(bb[p])+addOne
            if result >= 2:
                addOne = 1
                result -= 2
            else:
                addOne = 0
            ans.append(result)
        if addOne:
            ans.append(1)
        ans.reverse()
        
        return "".join(map(str,ans))
