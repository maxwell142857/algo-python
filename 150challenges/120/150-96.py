class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        visited = set()
        myQueue = []
        myQueue.append(startGene)
        visited.add(startGene)
        ans = 0
        while myQueue:
            newLevel = []
            ans += 1
            mutated = ['A','G','C','T']
            for current in myQueue:
                for i in range(8):
                    for j in range(4):
                        newOne = current[:i]+mutated[j]+current[i+1:]
                        if newOne not in visited and newOne in bank:
                            newLevel.append(newOne)
                            visited.add(newOne)
                            if newOne == endGene:
                                return ans
            myQueue = newLevel
        return -1