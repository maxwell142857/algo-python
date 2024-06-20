class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0,1,2]
        index = 3
        while index <= n:
            steps[index%3] = steps[(index+2)%3]+steps[(index+1)%3]
            index += 1
        return steps[n%3]