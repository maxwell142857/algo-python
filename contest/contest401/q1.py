class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        cnt = k//(n-1)
        k %= n-1
        if cnt%2==0:
            return k
        else:
            return n-k-1