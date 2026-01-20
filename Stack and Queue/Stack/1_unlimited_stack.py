class Stack:
    def __init__(self):
        self.stack = []  
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    # def __str__(self):
    #     return str(self.stack)


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print("Stack:", s.stack)
    print("Top element:", s.peek())
    print("Popped:", s.pop())
    print("Stack after pop:", s.stack)
    
