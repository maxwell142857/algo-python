class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        s2cnt = defaultdict(int)
        dicts = []
        for s in arr:
            mydict = defaultdict(int)
            for i in range(len(s)):
                for j in range(i+1,len(s)+1):
                    subs = s[i:j]
                    s2cnt[subs] += 1
                    mydict[subs] += 1
            dicts.append(mydict)
        
        result = []
        for i in range(len(arr)):
            s= arr[i]
            mydict = dicts[i]
            getResult = False
            for length in range(1,len(s)+1):
                candidates = []
                for start in range(len(s)):
                    if start+length<=len(s):
                        subs = s[start:start+length]
                        if s2cnt[subs]-mydict[subs] == 0:
                            candidates.append(subs)
                if candidates:
                    candidates.sort()
                    result.append(candidates[0])
                    getResult = True
                    break
            if not getResult:
                result.append('')
        return result
    


