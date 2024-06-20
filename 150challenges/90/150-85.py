from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        ans = []
        queue.append(root)
        left2right = True
        while len(queue) !=0:
            l = len(queue)
            level = []
            for _ in range(l):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if left2right:
                ans.append(level)
                left2right = False
            else:
                ans.append(level[::-1])
                left2right = True
        return ans