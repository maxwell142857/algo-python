class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cnt = numBottles
        remain = numBottles
        while remain>=numExchange:
            newB = remain//numExchange
            cnt += newB
            remain = remain-newB*numExchange+newB
        return cnt