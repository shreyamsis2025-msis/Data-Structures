class LimitedStack:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity
    
    def push(self, item):
        if self.size() >= self.capacity:
            raise OverflowError("Stack overflow: cannot push, stack is full")
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from empty stack")
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)


if __name__ == "__main__":
    s = LimitedStack(3) 
    s.push(10)
    s.push(20)
    s.push(30)
    print("Stack:", s.stack)

    try:
        s.push(40) 
    except OverflowError as e:
        print("Error:", e)

    print("Top element:", s.peek())
    print("Popped:", s.pop())
    print("Stack after pop:", s.stack)
