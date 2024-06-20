class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)

        def check(l):
            c2cnt = defaultdict(int)
            for i in range(l):
                c2cnt[s[i]] += 1
            for i in range(l,n,l):
                tmp = defaultdict(int)
                for j in range(l):
                    tmp[s[i+j]] += 1

                for key,val in tmp.items():
                    if c2cnt[key] != val:
                        return False
            return True
            
        
        for i in range(1,n+1):
            if n%i==0 and check(i):
                return i
        return -1
                