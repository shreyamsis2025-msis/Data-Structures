class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Insert element
    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full!")
            return

        if self.front == -1:  # first element
            self.front = 0
        
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

    # Remove element
    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty!")
            return

        removed = self.queue[self.front]

        if self.front == self.rear:  # last element removed
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return removed

    # Display queue
    def display(self):
        if self.front == -1:
            print("Queue is Empty")
            return

        i = self.front
        result = []

        while True:
            result.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size

        print("Circular Queue:", result)


# Example usage
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.dequeue()
cq.enqueue(60)
cq.display()
