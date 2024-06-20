class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        groupCnt = len(variables)
        ans = []
        for i in range(groupCnt):
            a = variables[i][0]
            b = variables[i][1]
            c = variables[i][2]
            m = variables[i][3]
            tmp = 1
            for _ in range(b):
                tmp = tmp*a%10
            tmp2 = 1
            for _ in range(c):
                tmp2 = tmp2*tmp%m
            if tmp2 == target:
                ans.append(i)
        return ans