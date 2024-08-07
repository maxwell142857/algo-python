import heapq as h
class Solution:
    # brute force
    # generate subArray's sum: O(n^2)
    # sort: O(n^2*logn)
    # compute sum: O(n^2)
    # total: O(n^2*logn)
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sumArray = []
        for start in range(n):
            curSum = 0
            for i in range(start,n):
                curSum += nums[i]
                sumArray.append(curSum)
        sumArray.sort()

        ans = 0
        MOD = 10**9+7
        for i in range(left-1,right):
            ans += sumArray[i]
            ans %= MOD
        return ans
    

    # heap, similiar to "merge k sorted list"
    # O(n^2*logn)
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        minHeap = []
        for i in range(n):
            h.heappush(minHeap,(nums[i],i))

        cnt = 0
        ans = 0
        MOD = 10**9+7
        while minHeap:
            val,index = h.heappop(minHeap)
            cnt += 1
            if cnt >= left:
                ans += val
                ans %= MOD
            if cnt == right:
                return ans
            
            if index != n-1:
                h.heappush(minHeap,(val+nums[index+1],index+1))
        
    # binary search + sliding windows
    # sliding windows:
    # for given val, get the cnt of subarray which sum <= val, O(n) 
    # also get total sum of subarray
    # binary search val, from 0 to sum(nums), O(log(sum(nums)))
    # total TC: O(nlog(sum(nums))) == O(nlog(n))

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # return the cnt and sum of subarray which sum(subarray)<= k
        def findSubArray(k):
            left = 0
            curSum = 0
            cnt = 0
            result = 0
            windowContribution = 0
            for right in range(n):
                curSum += nums[right]
                windowContribution += nums[right]*(right-left+1)
                while curSum > k:
                    windowContribution -= curSum
                    curSum -= nums[left]
                    left += 1
                result += windowContribution
                cnt += right-left+1
            # print(k,cnt,result)
            return [cnt,result]
        
        def fisrtKSum(index):
            left = low
            right = high
            while left < right:
                mid = (left+right)//2
                cnt,result = findSubArray(mid)
                if cnt >= index:
                    right = mid
                else:
                    left = mid+1
            cnt,result = findSubArray(left)
            # maybe we want find 3-th, however the firstKSum can only return 4
            # example: sum array:[1,1,2,2],findSubArray(2)=4,findSubArray(1)=2
            # so we remove the value(left is the value)
            more = cnt-index 
            return result-more*left
        low = min(nums)
        high = sum(nums)
        return (fisrtKSum(right)-fisrtKSum(left-1))%(10**9+7)
            

