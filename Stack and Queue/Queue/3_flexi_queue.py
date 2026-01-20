class FlexiQueue:
    def __init__(self, capacity=2):
        self.queue = []
        self.capacity = capacity
    
    def enqueue(self, item):
        if self.size() >= self.capacity:  # expand
            self.capacity *= 2
        self.queue.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self.queue.pop(0)
        if self.size() <= self.capacity // 4:  # shrink
            self.capacity //= 2
        return item
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def __str__(self):
        return f"Queue: {self.queue}, Capacity: {self.capacity}"


q = FlexiQueue()
for i in range(6):
    q.enqueue(i)
    print(q)
for _ in range(5):
    q.dequeue()
    print(q)
