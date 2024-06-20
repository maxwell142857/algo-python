class Solution:
    # hashmap
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        name2group = {}
        # group: [[person1's email],[person2's email],...]
        for content in accounts:
            name = content[0]
            mails = content[1:]
            if name not in name2group:
                name2group[name] = [set(mails)]
            else:
                groups = name2group[name]
                n = len(groups)
                mergeGroupName = []
                for i in range(n):
                    for mail in mails:
                        if mail in groups[i]:
                            mergeGroupName.append(groups[i])
                            break
                addSet = set(mails)
                for addGroup in mergeGroupName:
                    addSet |= addGroup
                    groups.remove(addGroup)
                groups.append(addSet)
        ans = []
        for key,value in name2group.items():
            for mailGroup in value:
                mailGroup = list(mailGroup)
                mailGroup.sort()
                mailGroup.insert(0,key)
                ans.append(mailGroup)
        return ans

    # graph
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = {}
        account2name = {}

        def addEdge(node1,node2):
            if node1 in graph:
                graph[node1].append(node2)
            else:
                graph[node1] = [node2]
            
            if node2 in graph:
                graph[node2].append(node1)
            else:
                graph[node2] = [node1]

        for acount in accounts:
            name = acount[0]
            email0 = acount[1]
            account2name[email0] = name
            if email0 not in graph:
                graph[email0] = []
            for email in acount[2:]:
                addEdge(email0,email)
                account2name[email] = name

        visited = set()
        tmp = []
        def DFS(node):
            visited.add(node)
            tmp.append(node)
            for son in graph[node]:
                if son not in visited:
                    DFS(son)
        
        ans = []
        for node in graph.keys():
            if node not in visited:
                DFS(node)
                tmp.sort()
                tmp.insert(0,account2name[tmp[0]])
                ans.append(tmp[:])
                tmp.clear()
        return ans


                

