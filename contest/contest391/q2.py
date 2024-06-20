class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drink = 0
        empty = 0
        while numBottles:
            drink += numBottles
            empty += numBottles
            numBottles = 0
            while empty >= numExchange:
                empty -= numExchange
                numExchange += 1
                numBottles += 1
        return drink