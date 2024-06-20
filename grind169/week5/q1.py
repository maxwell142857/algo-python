from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = {}
        for c in p:
            target[c] = target.get(c,0)+1
        
        delta = dict(target)
        ans = []
        n = len(s)
        left = 0
        right = 0
        while right < n:
            c = s[right]
            if c not in target:
                left = right+1
                right += 1
                delta = dict(target)
            else:
                if c in delta:
                    delta[c] -= 1
                    if delta[c] == 0:
                        del delta[c]
                        if len(delta)==0:
                            ans.append(left)
                            delta[s[left]] = 1
                            left += 1
                else:
                    while s[left] != c:
                        delta[s[left]] = delta.get(s[left],0)+1
                        left += 1
                    left += 1
                right += 1
        return ans