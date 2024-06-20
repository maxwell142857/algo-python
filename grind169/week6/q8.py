from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # BFS
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        ans = []
        queue.append((root,[],0))
        while queue:
            node = queue.popleft()
            path = node[1][:]
            path.append(node[0].val)
            sum = node[2]+node[0].val
            if not node[0].left and not node[0].right:
                # leave,check
                if sum == targetSum:
                    ans.append(path[:])
            if node[0].left:
                queue.append((node[0].left,path,sum))
            if node[0].right:
                queue.append((node[0].right,path,sum))
        return ans
    
    # DFS
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        path = []
        sum = 0
        ans = []

        def DFS(node):
            nonlocal path,sum
            path.append(node.val)
            sum += node.val

            if not node.left and not node.right:
                if sum == targetSum:
                    ans.append(path[:])
            
            if node.left:
                DFS(node.left)
            if node.right:
                DFS(node.right)
            path.pop()
            sum -= node.val
        
        DFS(root)
        return ans