class QueueUsingStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def enqueue(self, item):
        self.s1.append(item)
    
    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if not self.s2:
            raise IndexError("Queue is empty")
        return self.s2.pop()
    
    def __str__(self):
        return str(self.s1[::-1] + self.s2)


q = QueueUsingStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Queue:", q)
print("Dequeued:", q.dequeue())
print("Queue after dequeue:", q)
