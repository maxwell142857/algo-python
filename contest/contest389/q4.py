class Solution:
    # O(n^2), TLE
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:

        def merge(arr1,arr2):
            l1 = len(arr1)
            l2 = len(arr2)
            p1,p2 = 0,0
            result = []
            while p1<l1 and p2<l2:
                if arr1[p1]<arr2[p2]:
                    result.append(arr1[p1])
                    p1 += 1
                else:
                    result.append(arr2[p2])
                    p2 += 1
            if p1 == l1:
                result += arr2[p2:]
            else:
                result += arr1[p1:]
            return result
        
        def calculate(seq,twoCnt,target):
            if target <=0:
                return 0
            p = 0
            cnt = 0
            while p<len(seq) and seq[p]<2:
                cnt += seq[p]
                p += 1
                target -= 1
                if target==0:
                    return cnt
            while twoCnt > 0:
                cnt += 2
                twoCnt -= 1
                target -= 1
                if target==0:
                    return cnt
            while target > 0:
                cnt += seq[p]
                p += 1
                target -= 1
                if target==0:
                    return cnt
                
        def distance(arr):
            n = len(arr)
            result = []
            for i in range(n):
                if arr[i] == 1:
                    result.append(i+1)
            return result
        
        n = len(nums)
        ans = float('inf')
        for i in range(n):
            tmp = nums[:i]
            leftCnt = distance(tmp[::-1])
            rightCnt = distance(nums[i+1:])
            if nums[i] == 1:
                ans = min(ans,calculate(merge(leftCnt,rightCnt),maxChanges,k-1))
            else:
                ans = min(ans,calculate(merge(leftCnt,rightCnt),maxChanges,k))
        return ans
    
    # O(n) sliding windows+ preSum
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        oneIndex = []
        for i in range(len(nums)):
            if nums[i] == 1:
                oneIndex.append(i)
        
        preSum = oneIndex.copy()
        # preSum include itself
        for i in range(1,len(preSum)):
            preSum[i] += preSum[i-1]

        def getSum(left,right):
            # inclusive about left and right
            if left == 0:
                return preSum[right]
            else:
                return preSum[right]-preSum[left-1]
            
        def getDistance(left,right):
            # inclusive about left and right
            # choose mid point and then get distance
            # about each point to the mid
            mid = (left+right)//2
            
            result = 0
            # get all left points to mid
            result += oneIndex[mid]*(mid-left+1)-getSum(left,mid)
            # get all right points to mid
            result += getSum(mid+1,right)-oneIndex[mid]*(right-mid)
            return result
        
        ans = float('inf')
        if k-maxChanges<=0:
            ans = 2*k
        minWindowSize = min(1,k-maxChanges)
        # windowSize = count(actions2)
        # windowSize = k-maxChanges,means we use all maxchange
        # windowsize = k-maxChanges+3, means there are three point dont need to 
        for windowSize in range(minWindowSize,minWindowSize+4):
            if windowSize>k:
                break
            for left in range(len(oneIndex)):
                right = left+windowSize-1
                if right >= len(oneIndex):
                    break
                tmp = 0
                # cost use action1
                tmp += (k-windowSize)*2
                # cost use action2
                tmp += getDistance(left,right)
                ans = min(ans,tmp)
        

        return ans

        
