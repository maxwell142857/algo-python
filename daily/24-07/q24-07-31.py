class Solution:
    # search,O(2^n)
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        ans = 10**6+1
        def traverse(index,remainW,curH,val):
            nonlocal ans
            if index == n:
                ans = min(ans,val+curH)
                return
            
            w,h = books[index]
            if remainW<w:
                # we can only put it to next level
                traverse(index+1,shelfWidth-w,h,val+curH)
            else:
                # we can choose
                # next level
                traverse(index+1,shelfWidth-w,h,val+curH)
                # this level
                traverse(index+1,remainW-w,max(curH,h),val)

        traverse(0,shelfWidth,0,0)
        return ans
    
    # search -----> memory,O(n*w)
    # although in search method, we have 4 parameter def "traverse(index,remainW,curH,val)"
    # the last parameter is answer, we can use it as return value
    # the curH is based on index and remainW
    # which means that when we know index and remainW, the curH is a fix number
    # so the memo only need to be two dimension to record index and remain
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        memo = [[-1]*(shelfWidth+1) for _ in range(n)]

        def traverse(index,remainW,curH):
            if index == n:
                return curH
            if memo[index][remainW] != -1:
                return memo[index][remainW]
            
            w,h = books[index]
            if remainW<w:
                # we can only put it to next level
                memo[index][remainW] =  curH+traverse(index+1,shelfWidth-w,h)
            else:
                # we can choose
                # next level
                ans1 = curH+traverse(index+1,shelfWidth-w,h)
                # this level
                ans2 = traverse(index+1,remainW-w,max(curH,h))
                memo[index][remainW] = min(ans1,ans2)
            return memo[index][remainW]

        return traverse(0,shelfWidth,0)
    

    # dp
    # O(n*w)
    # def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
    #     n = len(books)
        
    #     dp = [10**6+1]*(n+1) # dp[i] means the cost when shelf end with (i-1)-th book
    #     dp[0] = 0
    #     dp[1] = books[0][1]
    #     for i in range(2,n+1):
    #         curLevelWidth = 0
    #         curLevelHeight = 0
    #         for j in range(i-1,-1,-1):
    #             curLevelWidth += books[j][0]
    #             curLevelHeight = max(curLevelHeight,books[j][1])
    #             if curLevelWidth>shelfWidth:
    #                 break
    #             dp[i] = min(dp[i],dp[j]+curLevelHeight)
    #     return dp[n]


