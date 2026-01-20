class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def is_empty(self):
        return len(self.stack) == 0

def transfer(S, T):
    temp = Stack()
    while not S.is_empty():
        temp.push(S.pop())
    while not temp.is_empty():
        T.push(temp.pop())


S = Stack()
T = Stack()
for i in [1, 2, 3, 4]:
    S.push(i)

transfer(S, T)
print("Stack T:", T.stack)  
