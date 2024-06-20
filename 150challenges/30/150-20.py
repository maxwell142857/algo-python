class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        n = len(strs)
        minLengh = len(strs[0])
        for i in range(1,n):
            minLengh = min(minLengh,len(strs[i]))

        for index in range(minLengh):
            target = strs[0][index]
            notMatch = False
            for strIndex in range(1,n):
                if strs[strIndex][index] != target:
                    notMatch = True
                    break

            if notMatch:
                break
            else:
                ans += target
        
        return ans