from collections import deque


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        myDeque = deque(tokens)
        score = 0
        ans = 0
        while myDeque and power>=myDeque[0]:
            while myDeque and power>=myDeque[0]:
                score += 1
                power -= myDeque[0]
                myDeque.popleft()
                ans = max(ans,score)
            if score>=1 and myDeque:
                score -= 1
                power += myDeque[-1]
                myDeque.pop()
        return ans
