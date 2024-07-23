class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aSum = sum(aliceSizes)
        bSum = sum(bobSizes)
        avg = (aSum+bSum)//2
        bobSizes = set(bobSizes)
        for val in aliceSizes:
            # avg-aSum = target-val
            if avg-aSum+val in bobSizes:
                return [val,avg-aSum+val]