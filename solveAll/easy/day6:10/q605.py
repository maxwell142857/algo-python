class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def canPlan(index):
            if flowerbed[index] == 1:
                return False
            if index-1>=0 and flowerbed[index-1] == 1:
                return False
            if index+1<len(flowerbed) and flowerbed[index+1] == 1:
                return False
            return True
        
        newFlowerCnt = 0
        for i in range(len(flowerbed)):
            if canPlan(i):
                newFlowerCnt += 1
                flowerbed[i] = 1
        return n <= newFlowerCnt

