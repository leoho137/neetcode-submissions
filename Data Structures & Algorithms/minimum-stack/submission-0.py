class MinStack:

    def __init__(self):
        self.stack = []
        self.minval = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minval:
            self.minval.append(min(val, self.minval[-1]))
        else:
            self.minval.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minval.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minval[-1]
        
