class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        array1 = version1.split('.')
        array2 = version2.split('.')
        n1 = len(array1)
        n2 = len(array2)
        if n1 > n2:
            array2.extend([0]*(n1-n2))
        else:
            array1.extend([0]*(n2-n1))
        n  = len(array1)
        p = 0
        while p<n:
            val1 = int(array1[p])
            val2 = int(array2[p])
            if val1>val2:
                return 1
            elif val1<val2:
                return -1
            else:
                p += 1
        return 0