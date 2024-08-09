class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c2cnt = defaultdict(int)
        for c in moves:
            c2cnt[c] += 1
        return c2cnt['L']==c2cnt['R'] and c2cnt['U']==c2cnt['D']