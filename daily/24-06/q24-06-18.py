class Solution:
    # memo, like preSum
    # O(m+n)
    # def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
    #     dMax = max(difficulty)
    #     money = [0]*(dMax+1)
    #     n = len(difficulty)
    #     for i in range(n):
    #         p = profit[i]
    #         d = difficulty[i]
    #         money[d] = max(money[d],p)

    #     for i in range(1,dMax+1):
    #         money[i] = max(money[i-1],money[i])
        
    #     ans = 0
    #     for w in worker:
    #         if w >= dMax:
    #             ans += money[-1]
    #         else:
    #             ans += money[w]
    #     return ans
    

    # O(nlog(n)+mlog(m))
    # sort+Bsearch
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        array = [[difficulty[i],profit[i]] for i in range(n)]
        array.sort()
        for i in range(1,n):
            array[i][1] = max(array[i][1],array[i-1][1])
        
        # TTTTFFFF,TTTT,FFFF
        def Bsearch(w):
            left = 0
            right = n-1
            while left<right:
                mid = (left+right+1)//2
                if array[mid][0]<=w:
                    left = mid
                else:
                    right = mid-1
            if array[left][0]>w:
                return 0
            else:
                return array[left][1]

        ans = 0
        for w in worker:
            ans += Bsearch(w)
        
        return ans
