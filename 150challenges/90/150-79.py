
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        pointer = root
        while pointer:
            self.stack.append(pointer)
            pointer = pointer.left
    def next(self) -> int:
        if len(self.stack) > 0:
            node = self.stack.pop()
            if node.right:
                pointer = node.right
                while pointer:
                    self.stack.append(pointer)
                    pointer = pointer.left
            return node.val
        else:
            return -1

    def hasNext(self) -> bool:
        return len(self.stack) > 0
            
            