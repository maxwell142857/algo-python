class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        array = []
        for i in range(n):
            array.append([heights[i],names[i]])
        array.sort(key = lambda x:-x[0])
        return [val[1] for val in array]