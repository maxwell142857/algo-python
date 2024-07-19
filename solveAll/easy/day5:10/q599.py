class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        s2index = {}
        s2val = {}
        for i in range(len(list1)):
            s2index[list1[i]] = i

        for i in range(len(list2)):
            s = list2[i]
            if s in s2index:
                s2val[s] = s2index[s]+i
        
        leastIndex = min(s2val.values())
        ans = []
        for k,v in s2val.items():
            if v == leastIndex:
                ans.append(k)
        return ans