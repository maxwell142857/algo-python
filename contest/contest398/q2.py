class Solution:
    # brute force
    # O(m*n)
    # TLE
    # def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
    #     def check(start,end):
    #         for i in range(start,end):
    #             if (nums[i]+nums[i+1])%2 == 0:
    #                 return False
    #         return True
        
    #     ans = []
    #     for s,e in queries:
    #         ans.append(check(s,e))
    #     return ans
    
    # O(log(n)*m)
    # def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
    #     # we dont care number, instead, we care the connection between number
    #     # so we record whether the connection is legal
    #     n = len(nums)
    #     connections = [] # connections[i] means connection between nums[i] and nums[i+1]
    #     for i in range(n-1):
    #         if (nums[i]+nums[i+1])%2 == 0:
    #             connections.append(False)
    #         else:
    #             connections.append(True)
    #     falseIndex = [i for i in range(n-1) if not connections[i]]
    #     falseCnt = len(falseIndex)

    #     # log(n)
    #     def check(start,end):
    #         if start == end:
    #             return True
    #         # nums[start] to nums[end] --> connections[start] to connections[end-1]

    #         # use binary search to find the first falseIndex i such that i >= start
    #         left = 0
    #         right = falseCnt
    #         while left < right:
    #             mid = (left+right)//2
    #             if falseIndex[mid] == start:
    #                 break
    #             elif falseIndex[mid] > start:
    #                 right = mid
    #             else:
    #                 left = mid+1

    #         if left == falseCnt:
    #             # we can not find a false connection
    #             # this interval is safe
    #             return True
    #         else:
    #             # if the end is small than firstFalseIndex, the interval is safe
    #             firstFalseIndex = falseIndex[left]
    #             return end-1 <firstFalseIndex
        
    #     ans = []
    #     for s,e in queries:
    #         ans.append(check(s,e))
    #     return ans

    # preSum
    # O(m+n)
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        illegalCnt = [0]*n
        # illegalCnt[i] means before i-th element(inclusive), how many illegal connection
        for i in range(1,n):
            if (nums[i]+nums[i-1])%2 == 0:
                illegalCnt[i] = illegalCnt[i-1]+1
            else:
                illegalCnt[i] = illegalCnt[i-1]

        # O(1)
        def check(start,end):
            return illegalCnt[start] == illegalCnt[end]
        
        ans = []
        for s,e in queries:
            ans.append(check(s,e))
        return ans