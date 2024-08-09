class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        isPositive = True
        up,down = False,False
        for i in range(1,n):
            pre = arr[i-1]
            cur = arr[i]
            if pre>cur:
                down = True
            elif pre<cur:
                up = True

            if isPositive:
                if pre < cur:
                    continue
                elif pre == cur:
                    return False
                else:
                    isPositive = False
            else:
                if pre <= cur:
                    return False
                else:
                    continue
        return up and down
