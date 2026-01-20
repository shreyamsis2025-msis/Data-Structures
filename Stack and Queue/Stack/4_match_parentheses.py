class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def is_empty(self):
        return len(self.stack) == 0

def match_parentheses(expr):
    s = Stack()
    for ch in expr:
        if ch == "(":
            s.push(ch)
        elif ch == ")":
            if s.is_empty():
                return False
            s.pop()
    return s.is_empty()

print(match_parentheses("(a+b)*(c+d)")) 
print(match_parentheses("((a+b)") )      
