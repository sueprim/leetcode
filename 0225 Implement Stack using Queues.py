from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0

stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
print("pop: ", stack.pop()) 
print("top: ", stack.top()) 
while not stack.empty():
    print("Popped element: ", stack.pop())
print("Is stack empty?", stack.empty()) 