class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def is_empty(self):
        return len(self.stack) == 0

def reverse_file(input_file, output_file):
    s = Stack()
    
    with open(input_file, "r") as f:
        for line in f:
            s.push(line.strip())
    
    with open(output_file, "w") as f:
        while not s.is_empty():
            f.write(s.pop() + "\n")

reverse_file("Stack\input.txt", "Stack\\reversed.txt")
