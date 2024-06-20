class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        bank = set(wordList)
        wordLength = len(beginWord)
        visited = set()
        myQueue = []
        myQueue.append(beginWord)
        visited.add(beginWord)
        ans = 0
        while myQueue:
            newLevel = []
            ans += 1
            for current in myQueue:
                for i in range(wordLength):
                    for j in range(26):
                        newOne = current[:i]+chr(ord('a')+j)+current[i+1:]
                        if newOne not in visited and newOne in bank:
                            newLevel.append(newOne)
                            visited.add(newOne)
                            if newOne == endWord:
                                return ans+1
            myQueue = newLevel
        return 0