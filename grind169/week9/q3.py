from collections import Counter
class Solution:
    # O(n^2),TLE
    # def minWindow(self, s: str, t: str) -> str:
    #     def containAll(superSet,subSet):
    #         for key,val in subSet.items():
    #             if key in superSet and superSet[key] >= val:
    #                 continue
    #             else:
    #                 return False
    #         return True
        
    #     c2cnt = Counter(t)
        
    #     ans = None
    #     n = len(s)
    #     for i in range(n):
    #         state = defaultdict(int)
    #         for j in range(n):
    #             if i+j == n or (ans!=None and j+1>len(ans)):
    #                 break
    #             state[s[i+j]] += 1
    #             if containAll(state,c2cnt):
    #                 ans = s[i:i+j+1]
    #                 break
    #     if ans:
    #         return ans
    #     else:
    #         return ''

    # sliding windows,O(n)
    # def minWindow(self, s: str, t: str) -> str:
    #     def containAll(superSet,subSet):
    #         for key,val in subSet.items():
    #             if key in superSet and superSet[key] >= val:
    #                 continue
    #             else:
    #                 return False
    #         return True
        
    #     c2cnt = Counter(t)
        
    #     ans = None
    #     n = len(s)
    #     left = 0
    #     state = defaultdict(int)
    #     for right in range(n):
    #         state[s[right]] += 1
                
    #         while containAll(state,c2cnt):
    #             if (not ans) or (right-left+1<len(ans)):
    #                 ans = s[left:right+1]
    #             state[s[left]] -= 1
    #             left += 1
                
            
    #     if ans:
    #         return ans
    #     else:
    #         return ''
        
    # sliding windows,O(n)，constant factor optimization
    def minWindow(self, s: str, t: str) -> str:
        c2cnt = Counter(t)
        requireCnt = len(c2cnt)
        tmpCnt = 0
        ans = None
        n = len(s)
        left = 0
        state = defaultdict(int)
        for right in range(n):
            c = s[right]
            state[c] += 1
            if state[c] == c2cnt[c]:
                tmpCnt += 1
            while tmpCnt == requireCnt:
                if (not ans) or (right-left+1<ans[1]-ans[0]+1):
                    ans = (left,right)
                state[s[left]] -= 1
                if s[left] in c2cnt and state[s[left]]==c2cnt[s[left]]-1:
                    tmpCnt -= 1
                left += 1
            
        if ans:
            return s[ans[0]:ans[1]+1]
        else:
            return ''