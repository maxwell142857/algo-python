class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        ans = 0
        for start in range(n):
            used = set()
            hashmap = {}
            for length in range(1,n-start+1):
                # check the diff
                if length != 1:
                    if abs(ord(word[start+length-1])-ord(word[start+length-2])) > 2:
                        break
                # check the count
                char = word[start+length-1]
                if char in used:
                    break
                else:
                    if char in hashmap:
                        hashmap[char] -= 1
                    else:
                        hashmap[char] = k-1
                    if hashmap[char] == 0:
                        used.add(char)
                        del hashmap[char]
                if length%k == 0:
                    if len(hashmap) == 0:
                        ans += 1
        return ans
    
s = Solution()
s.countCompleteSubstrings("igigee",2)