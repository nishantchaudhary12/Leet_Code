'''Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.'''


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = list()

    def push(self, x: int) -> None:
        if self.head:
            self.head.append((x, min(x, self.getMin())))
        else:
            self.head.append((x, x))

    def pop(self) -> None:
        if not self.head:
            return None
        self.head.pop()

    def top(self) -> int:
        if not self.head:
            return None
        return self.head[-1][0]

    def getMin(self) -> int:
        if not self.head:
            return None
        return self.head[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()