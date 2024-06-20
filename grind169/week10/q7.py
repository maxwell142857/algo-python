from collections import deque,defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        inDegree = defaultdict(int)

        charSet = set()
        for w in words:
            for c in w:
                charSet.add(c)

        # return if this situation already break the rule. EG: ["abc","ab"]
        def getOrder(w1,w2):
            n1 = len(w1)
            n2 = len(w2)
            p1,p2=0,0
            while p1<n1 and p2<n2:

                if w1[p1] != w2[p2]:
                    if w2[p2] not in graph[w1[p1]]:
                        graph[w1[p1]].add(w2[p2])
                        inDegree[w2[p2]] += 1
                    return True
                p1 += 1
                p2 += 1
            if n1 > n2:
                return False
            else:
                return True

        n = len(words)
        for i in range(n-1):
            if not getOrder(words[i],words[i+1]):
                return ''
        
        myList = deque()
        for c in charSet:
            if c not in inDegree:
                myList.append(c)
        
        order = []
        while myList:
            l = len(myList)
            for _ in range(l):
                cur = myList.popleft()
                order.append(cur)
                for son in graph[cur]:
                    inDegree[son] -= 1
                    if inDegree[son] == 0:
                        myList.append(son)
        
        # check whether all node is deleted
        for k,v in inDegree.items():
            if v != 0:
                return ''
        return ''.join(order)                


        
        