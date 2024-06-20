from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def isConnected(s1,s2):
            n = len(s1)
            diffCnt = 0
            for i in range(n):
                if s1[i] != s2[i]:
                    diffCnt += 1
                if diffCnt == 2:
                    return False
            return True
        
        visited = set()
        n = len(wordList)
        # run bfs 
        level = deque()
        level.append(beginWord)
        wordCnt = 1
        while level:
            l = len(level)
            for _ in range(l):
                cur = level.popleft()
                if cur == endWord:
                    return wordCnt
                # find all adjacent words
                for i in range(n):
                    if wordList[i] not in visited and isConnected(cur,wordList[i]):
                        level.append(wordList[i])
                        visited.add(wordList[i])
            wordCnt += 1
        return 0