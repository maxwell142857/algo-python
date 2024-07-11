class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curT = 0
        waitT = 0
        n = len(customers)
        for arrive,t in customers:
            if arrive < curT:
                waitT += curT-arrive
                waitT += t
                curT += t
            else:
                waitT += t
                curT = arrive+t
        return waitT/n

