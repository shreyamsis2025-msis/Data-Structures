# def remove_odds_circular(head):
#     if not head:
#         return None

#     dummy = Node(0)
#     dummy.next = head
#     prev, curr = dummy, head

#     while True:
#         if curr.data % 2 != 0:
#             prev.next = curr.next
#             if curr.next == head:  # if we delete head
#                 head = curr.next
#         else:
#             prev = curr
#         curr = curr.next
#         if curr == head:
#             break

#     return head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_circular_list(values):
    """Helper to create circular linked list from list of values"""
    if not values:
        return None
    head = Node(values[0])
    temp = head
    for val in values[1:]:
        temp.next = Node(val)
        temp = temp.next
    temp.next = head  # make it circular
    return head

def display_circular(head, count=10):
    """Helper to display circular list (limited by count to avoid infinite loop)"""
    if not head:
        print("Empty List")
        return
    temp = head
    c = 0
    while c < count:
        print(temp.data, end=" -> ")
        temp = temp.next
        c += 1
    print("... (circular)")

def remove_odds_circular(head):
    if not head:
        return None

    # Handle case where all elements are odd
    temp = head
    all_odd = True
    while True:
        if temp.data % 2 == 0:
            all_odd = False
            break
        temp = temp.next
        if temp == head:
            break
    if all_odd:
        return None

    # Remove odd nodes
    dummy = Node(0)
    dummy.next = head
    prev, curr = dummy, head
    while True:
        if curr.data % 2 != 0:  # odd → remove
            prev.next = curr.next
            if curr == head:     # if head is odd
                head = curr.next
        else:
            prev = curr
        curr = curr.next
        if curr == head:
            break

    return head

# 🔹 Example Run
head = create_circular_list([1, 2, 3, 4, 5, 6])
print("Original Circular List:")
display_circular(head)

head = remove_odds_circular(head)
print("After Removing Odd Elements:")
display_circular(head)
