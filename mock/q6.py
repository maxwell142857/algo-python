# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # check special situation, just one line
        if numRows == 1:
            return s
        
        lines = [[] for _ in range(numRows)]
        index = 0
        direction = 1 # 1 means add, -1 means minus
        for c in s:
            lines[index].append(c)
            # check whether reach the boundary
            if index == numRows-1 and direction == 1:
                direction = -1
            elif index == 0 and direction ==-1:
                direction = 1
            # change the index
            index += direction
        
        result = ''
        for line in lines:
            result += ''.join(line)
        return result

s = Solution()
test1 = 'ABC'
print(s.convert(test1,1))