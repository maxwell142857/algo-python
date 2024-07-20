class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(c for c in jewels)
        cnt = 0
        for stone in stones:
            if stone in jewels:
                cnt += 1
        return cnt