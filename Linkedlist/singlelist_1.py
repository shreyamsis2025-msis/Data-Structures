class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    # a. Add at head
    def add_at_head(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    # b. Add at tail
    def add_at_tail(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return 
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    # c. Delete at head
    def delete_at_head(self):
        if self.head:
            self.head = self.head.next

    # d. Delete at tail
    def delete_at_tail(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    # e. Add after given data
    def add_after(self, key, data):
        temp = self.head
        while temp:
            if temp.data == key:
                new = Node(data)
                new.next = temp.next
                temp.next = new
                return
            temp = temp.next

    # f. Delete after given data
    def delete_after(self, key):
        temp = self.head
        while temp and temp.next:
            if temp.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next

    # g. Search element
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# sll = SingleLinkedList()
# sll.add_at_head(10)
# sll.add_at_tail(20)
# sll.add_at_tail(30)
# sll.add_after(20, 25)
# print("Initial List:")
# sll.display()

# sll.delete_at_head()
# sll.delete_after(20)
# print("After Deletions:")
# sll.display()

# print("Search 25:", sll.search(25))
# print("Search 30:", sll.search(30))