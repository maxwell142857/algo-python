class StringIterator:

    def __init__(self, s: str):
        n = len(s)
        p = 0
        cnt = 0
        char = ''
        self.array = []
        while p<n:
            c = s[p]
            if c.isnumeric():
                while p<n and s[p].isnumeric():
                    cnt *= 10
                    cnt += int(s[p])
                    p += 1
                self.array.append([char,cnt])
                cnt = 0
                char = ''
            else:
                char = c
                p += 1
        

        self.p = 0
        self.val = 0
    def next(self) -> str:
        if self.hasNext():
            ans = self.array[self.p][0]
            self.val += 1
            if self.val == self.array[self.p][1]:
                self.p += 1
                self.val = 0
            return ans
        else:
            return ' '

    def hasNext(self) -> bool:
        return self.p<len(self.array)


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()