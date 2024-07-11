class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0
        for log in logs:
            if log == '../':
                cnt = max(0,cnt-1)
            elif log == './':
                pass
            else:
                cnt += 1
        return cnt
