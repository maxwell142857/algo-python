class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        tmp = []
        for row in mat:
            for val in row:
                tmp.append(val)
        if len(tmp) != r*c:
            return mat
        
        ans = []
        for i in range(r):
            ans.append(tmp[i*c:(i+1)*c])
        return ans