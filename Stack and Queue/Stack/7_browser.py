class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop() if not self.is_empty() else None
    def is_empty(self):
        return len(self.stack) == 0

class Browser:
    def __init__(self):
        self.back_stack = Stack()
        self.forward_stack = Stack()
        self.current = None
    
    def visit(self, url):
        if self.current:
            self.back_stack.push(self.current)
        self.current = url
        self.forward_stack = Stack()  
        print("Visited:", url)
    
    def back(self):
        if self.back_stack.is_empty():
            print("No back history")
            return
        self.forward_stack.push(self.current)
        self.current = self.back_stack.pop()
        print("Back to:", self.current)
    
    def forward(self):
        if self.forward_stack.is_empty():
            print("No forward history")
            return
        self.back_stack.push(self.current)
        self.current = self.forward_stack.pop()
        print("Forward to:", self.current)


b = Browser()
b.visit("a.com")
b.visit("b.com")
b.visit("c.com")
b.back()
b.back()
b.forward()
