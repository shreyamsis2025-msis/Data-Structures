from singlelist_1 import SingleLinkedList
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

lst = SingleLinkedList()
for val in [1, 2, 3, 4]:
    lst.add_at_tail(val)

print("List:")
lst.display()
print("Has Cycle?", has_cycle(lst.head))

# Manually creating cycle
lst.head.next.next.next.next = lst.head.next
print("Has Cycle after adding cycle?", has_cycle(lst.head))