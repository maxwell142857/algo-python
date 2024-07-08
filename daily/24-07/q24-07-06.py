class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        round = n-1
        cnt = time//round
        time -= cnt*round
        if cnt%2==0:
            return 1+time
        else:
            return n-time