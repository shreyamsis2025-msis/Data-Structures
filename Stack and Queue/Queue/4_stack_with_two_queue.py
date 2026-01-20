from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    
    def push(self, item):
        self.q1.append(item)
    
    def pop(self):
        if not self.q1:
            raise IndexError("Stack is empty")
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        popped = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return popped
    
    def __str__(self):
        return str(list(self.q1))


s = StackUsingQueues()
s.push(10)
s.push(20)
s.push(30)
print("Stack:", s)
print("Popped:", s.pop())
print("Stack after pop:", s)
