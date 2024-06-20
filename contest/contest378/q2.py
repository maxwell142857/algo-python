class Solution:
    def maximumLength(self, s: str) -> int:
        def check(length):
            s2cnt = {} # key: string, value:appear times
            for start in range(0,len(s)-length+1):
                tmp = s[start:start+length]
                if len(set(list(tmp))) == 1:
                    if tmp not in s2cnt:
                        s2cnt[tmp] = 1
                    else:
                        s2cnt[tmp] += 1
                        if s2cnt[tmp] == 3:
                            print(tmp)
                            return True
            return False
        
        left = 1
        right = len(s)
        while(left<right):
            mid = (left+right+1)//2
            if check(mid):
                left = mid
            else:
                right = mid-1
        
        if left == 1:
            if check(1):
                return 1
            else:
                return -1
        else:
            return left
        
s = Solution()
print(s.maximumLength("cccerrrecdcdccedecdcccddeeeddcdcddedccdceeedccecde"))