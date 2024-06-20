class Solution:
    # greedy, first add small box
    # O(nlog(n)+mlog(m))
    # def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        
        # def store(box,space):
        #     box.sort()
        #     space.sort()
        #     lB = len(box)
        #     lS = len(space)
        #     pB,pS = 0,0
        #     cnt = 0
        #     while pB<lB and pS<lS:
        #         if box[pB] <= space[pS]:
        #             cnt += 1
        #             pB += 1
        #             pS += 1
        #         else:
        #             pS += 1
        #     return cnt
        
    #     # find the smallest value's index
    #     minSpace = min(warehouse)
    #     p = 0
    #     while True:
    #         if warehouse[p] != minSpace:
    #             p += 1
    #         else:
    #             break
        
    #     spaces = []
    #     preH = max(warehouse)
    #     # add item from left
    #     for i in range(p+1):
    #         if warehouse[i]<=preH:
    #             spaces.append(warehouse[i])
    #             preH = warehouse[i]
    #         else:
    #             spaces.append(preH)
    #     # add item from right
    #     preH = max(warehouse)
    #     for i in range(len(warehouse)-1,p,-1):
    #         if warehouse[i]<=preH:
    #             spaces.append(warehouse[i])
    #             preH = warehouse[i]
    #         else:
    #             spaces.append(preH)

    #     return store(boxes,spaces)   
    
    # greedy,first add large box
    # O(nlog(n))
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort(reverse=True)
        lB = len(boxes)
        lW = len(warehouse)
        left,right = 0,lW-1
        p = 0
        cnt = 0
        while left<=right and p < lB:
            # put current box from left
            if warehouse[left]>= boxes[p]:
                cnt += 1
                p += 1
                left += 1
            elif warehouse[right]>= boxes[p]:
                cnt += 1
                p += 1
                right -= 1
            else:
                p += 1
        return cnt

