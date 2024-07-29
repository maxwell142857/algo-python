class Solution:
    # O(n^2)
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        leftLess = [0]*n
        for i in range(n):
            cnt = 0
            for j in range(i):
                if rating[j] < rating[i]:
                    cnt += 1
            leftLess[i] = cnt
        
        rightLess = [0]*n
        for i in range(n-1,-1,-1):
            cnt = 0
            for j in range(i+1,n):
                if rating[j]<rating[i]:
                    cnt += 1
            rightLess[i] = cnt
        
        ans = 0
        for i in range(n):
            ans += leftLess[i]*(n-i-1-rightLess[i])
            ans += (i-leftLess[i])*rightLess[i]
        return ans