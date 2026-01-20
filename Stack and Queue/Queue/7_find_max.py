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
    
    def size(self):
        return len(self.queue)
    
    def findMax(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        max_val = max(self.queue)
        return max_val
    
    def __str__(self):
        return str(self.queue)


q = Queue()
for i in [5, 3, 8, 2, 7]:
    q.enqueue(i)

print("Queue:", q)
print("Max element:", q.findMax())
print("Queue after findMax (unchanged):", q)
