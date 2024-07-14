class Solution:
    def minimumCost(self, m: int, n: int, g1: List[int], g2: List[int]) -> int:
        g1.sort()
        g2.sort()
        multi1,multi2 = 1,1
        cost = 0
        while g1 and g2:
            if g1[-1] < g2[-1]:
                removeVal = g2.pop()
                cost += multi2*removeVal
                multi1 += 1
            else:
                removeVal = g1.pop()
                cost += multi1*removeVal
                multi2 += 1
        cost += multi1*sum(g1)+multi2*sum(g2)
        return cost