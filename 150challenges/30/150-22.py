import math
class Solution:
    # stupid method
    # def convert(self, s: str, numRows: int) -> str:
    #     if numRows == 1:
    #         return s
    #     n = len(s)
    #     hashmap = {}
    #     hashmap[1002] = s[0]
    #     row = 1
    #     col = 1
    #     count = 1
    #     isDown = True
    #     for i in range(1,n):
    #         if count == numRows:
    #             isDown = not isDown
    #             count = 1
    #         if isDown:
    #             row += 1
    #         else:
    #             row -= 1
    #             col += 1
    #         hashmap[row*1001+col] = s[i]
    #         count += 1

    #     ans = ""
    #     maxCol = math.ceil(n/(2*numRows-2))*(numRows-1)
    #     for i in range(1,numRows+1):
    #         for j in range(1,maxCol+1):
    #             if(i*1001+j in hashmap):
    #                 ans += hashmap[i*1001+j]

    #     return ans
    # clever method
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        lines = [[] for _ in range(numRows)]
        index = 0
        increase = True
        for i in range(n):
            lines[index].append(s[i])
            if index==numRows-1:
                increase = False
            if index==0:
                increase = True
            index = index+1 if increase else index-1
        ans = ""
        for i in range(numRows):
            ans += "".join(lines[i])
        return ans

solution = Solution()
print(solution.convert('PAYPALISHIRING',4))


# P   A   H   N
# A P L S I I G
# Y   I   R
