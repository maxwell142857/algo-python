class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for op in operations:
            if op == '+':
                ans.append(ans[-1]+ans[-2])
            elif op == 'D':
                ans.append(ans[-1]*2)
            elif op == 'C':
                ans.pop()
            else:
                ans.append(int(op))
        return sum(ans)