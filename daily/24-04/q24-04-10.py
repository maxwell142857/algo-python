from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        simulation = [i for i in range(n)]
        simulation = deque(simulation)
        order = []
        while simulation:
            order.append(simulation.popleft())
            if simulation:
                simulation.append(simulation.popleft())
        deck.sort()
        ans = [0]*n
        for i in range(n):
            num = deck[i]
            index = order[i]
            ans[index] = num
        return ans