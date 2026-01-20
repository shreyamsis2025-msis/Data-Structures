class LimitedQueue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity
    
    def enqueue(self, item):
        if self.size() >= self.capacity:
            raise OverflowError("Queue overflow: cannot enqueue, queue is full")
        self.queue.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from empty queue")
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def __str__(self):
        return str(self.queue)


q = LimitedQueue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Queue:", q)

try:
    q.enqueue(4)
except OverflowError as e:
    print("Error:", e)
