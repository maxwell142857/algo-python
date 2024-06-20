from collections import OrderedDict
class Solution:
    # o(n^2)，MLE
    # def medianOfUniquenessArray(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     cnt = []
    #     for i in range(n):
    #         have = set()
    #         for j in range(i,n):
    #             have.add(nums[j])
    #             cnt.append(len(have))
        
    #     cnt.sort()
    #     hl = len(cnt)//2
    #     if len(cnt)%2==0:
    #         return cnt[hl-1]
    #     else:
    #         return cnt[hl]
        
    # O(n^2)，space optimization, TLE
    # def medianOfUniquenessArray(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     cnt = OrderedDict()
    #     for i in range(n):
    #         have = set()
    #         for j in range(i,n):
    #             have.add(nums[j])
    #             l = len(have)
    #             if l in cnt:
    #                 cnt[l] += 1
    #             else:
    #                 cnt[l] = 1

    #     totalCnt = n*(n+1)//2
    #     if totalCnt%2 == 0:
    #         targetCnt = totalCnt//2
    #     else:
    #         targetCnt = totalCnt//2+1
    #     curCnt = 0
    #     for k,v in cnt.items():
    #         curCnt += v
    #         if curCnt>=targetCnt:
    #             return k
            
    # O(n^2) binary search + sliding windows
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        def atMostK(k):
            cnt = 0
            left = 0
            num2cnt = defaultdict(int)
            for right in range(len(nums)):
                num2cnt[nums[right]] += 1
                while len(num2cnt) > k:
                    leftNum = nums[left]
                    num2cnt[leftNum] -= 1
                    if num2cnt[leftNum] == 0:
                        del num2cnt[leftNum]
                    left += 1
                cnt += right-left+1
            return cnt
        
        # use binary search
        n = len(nums)
        left = 0
        right = n
        while left < right:
            mid = (left+right)//2
            order = atMostK(mid)
            if order>=n*(n+1)//2-order:
                right = mid
            else:
                left = mid+1
        return left

