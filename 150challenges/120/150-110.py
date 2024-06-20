class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def getNode(leftR,leftC,rightR,rightC):
            node = Node(0,0,None,None,None,None)
            if leftR == rightR and leftC == rightC:
                node.val = grid[leftR][leftC]
                node.isLeaf = 1
                return node
            
            midR = (leftR+rightR)//2
            midC = (leftC+rightC)//2
            topLeft = getNode(leftR,leftC,midR,midC)
            topRight = getNode(leftR,midC+1,midR,rightC)
            bottomLeft = getNode(midR+1,leftC,rightR,midC)
            bottomRight = getNode(midR+1,midC+1,rightR,rightC)

            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and \
            topLeft.val == topRight.val and topLeft.val == bottomLeft.val and topLeft.val == bottomRight.val:
                node.isLeaf = 1
                node.val = topLeft.val
                return node
            else:
                node.topLeft = topLeft
                node.topRight = topRight
                node.bottomLeft = bottomLeft
                node.bottomRight = bottomRight
                return node

        return getNode(0,0,n-1,n-1)

