class Solution:
    # O(26*n),as need to check with every character using sliding windows
    def characterReplacement(self, s: str, k: int) -> int:
        # input a binary array, return the length of subarray with at most k 0
        def mostK(arr):
            n = len(arr)
            left = 0
            cnt = 0
            maxL = 0
            for right in range(n):
                if arr[right] == 0:
                    cnt += 1
                if cnt > k:
                    while arr[left] != 0:
                        left += 1
                    left += 1
                    cnt -= 1
                maxL = max(maxL,right-left+1)
            return maxL
        
        n = len(s)
        ans = 0
        ascA = ord('A')
        ascZ = ord('Z')
        for i in range(ascA,ascZ+1):
            target = chr(i)
            array = []
            for c in s:
                if c == target:
                    array.append(1)
                else:
                    array.append(0)
            ans = max(ans,mostK(array))
        return ans
    # O(n),using sliding windows directly,the thinking is quite different from normal sliding windows
    # the subarray inside the windows might be invalid
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        c2cnt = defaultdict(int)
        maxF = 0
        ans = 0
        for right in range(n):
            c = s[right]
            c2cnt[c] += 1
            maxF = max(maxF,c2cnt[c])
            if maxF+k < right-left+1:
                c2cnt[s[left]] -= 1
                left += 1
            ans = max(ans,right-left+1)
        return ans