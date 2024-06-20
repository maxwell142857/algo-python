from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        queue = deque()
        ans = []
        queue.append(root)
        while len(queue) !=0:
            l = len(queue)
            sum = 0
            cnt = 0
            for _ in range(l):
                node = queue.popleft()
                sum += node.val
                cnt += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(sum/cnt)
        return ans