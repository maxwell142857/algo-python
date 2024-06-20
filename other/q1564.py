class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # box and space is in ascending order
        def store(box,space):
            lB = len(box)
            lS = len(space)
            pB,pS = 0,0
            cnt = 0
            while pB<lB and pS<lS:
                if box[pB] <= space[pS]:
                    cnt += 1
                    pB += 1
                    pS += 1
                else:
                    pS += 1
            return cnt
        
        preH = max(warehouse)
        for i in range(len(warehouse)):
            warehouse[i] = min(warehouse[i],preH)
            preH = warehouse[i]
        boxes.sort()
        return store(boxes,warehouse[::-1])

        
