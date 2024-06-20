class Solution:
    # brute force,O(n^2),TLE
    # def wonderfulSubstrings(self, word: str) -> int:
    #     n = len(word)
    #     ans = 0
    #     for i in range(n):
    #         c2cnt = defaultdict(int)
    #         illegalCnt = 0
    #         for j in range(i,n):
    #             c2cnt[word[j]] += 1
    #             if c2cnt[word[j]]%2==0:
    #                 illegalCnt -= 1
    #             else:
    #                 illegalCnt += 1
    #             if illegalCnt<=1:
    #                 ans += 1
    #     return ans


    # preSum+bitmask,O(n)
    def wonderfulSubstrings(self, word: str) -> int:
        n = len(word)
        ans = 0
        bitmask = 0
        mask2cnt = defaultdict(int)
        mask2cnt[bitmask] = 1
        for i in range(n):
            delta = ord(word[i])-ord('a')
            # if this bit is set 1, change it to 0;else change it to 1
            bitmask ^= (1<<delta)
            
            # find all pre bitmask' which are same as current one 
            ans += mask2cnt[bitmask]
            # find all pre bitmask' which are different from current one by 1 bit
            for j in range(10):
                mutation = bitmask ^ (1<<j)
                ans += mask2cnt[mutation]
            # add current mask into hashmap
            mask2cnt[bitmask] += 1
        return ans