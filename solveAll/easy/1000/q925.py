class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        def s2array(s):
            result = [] # [char,cnt]
            for c in s:
                if not result or c != result[-1][0]:
                    result.append([c,1])
                else:
                    result[-1][1] += 1
            return result

        array1 = s2array(name)
        array2 = s2array(typed)
        if len(array1) != len(array2):
            return False
        n = len(array1)
        for i in range(n):
            if array1[i][0] != array2[i][0] or array1[i][1]>array2[i][1]:
                return False
        return True