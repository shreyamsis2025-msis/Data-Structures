class SimpleQueue:
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
    
    def size(self):
        return len(self.queue)
    
    def __str__(self):
        return str(self.queue)



q = SimpleQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Queue:", q)
print("Dequeued:", q.dequeue())
print("Queue after dequeue:", q)
