class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def rotate(self):
        self.queue.reverse()
    
    def __str__(self):
        return str(self.queue)


q = Queue()
for i in [1, 2, 3, 4]:
    q.enqueue(i)

print("Queue:", q)
q.rotate()
print("Queue after rotate:", q)
