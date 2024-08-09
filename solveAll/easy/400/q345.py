class Solution:

    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        v = []
        for c in s:
            if c in vowels:
                v.append(c)
        v = v[::-1]
        pv = 0
        ans = []
        for c in s:
            if c in vowels:
                ans.append(v[pv])
                pv += 1
            else:
                ans.append(c)
        return ''.join(ans)
    
    # two pointers, save space
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        ans = []
        n = len(s)
        p = n-1
        while p>=0 and s[p] not in vowels:
            p -= 1
        for c in s:
            if c not in vowels:
                ans.append(c)
            else:
                ans.append(s[p])
                p -= 1
                while p>=0 and s[p] not in vowels:
                    p -= 1
        return ''.join(ans)

        