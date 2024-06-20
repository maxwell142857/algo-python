class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0 or self.minStack[-1] >= val:
            self.minStack.append(val)

    def pop(self) -> None:
        val = self.stack[-1]
        del self.stack[-1]
        if val == self.minStack[-1]:
            del self.minStack[-1]
        return val


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]