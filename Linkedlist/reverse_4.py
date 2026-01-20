from singlelist_1 import SingleLinkedList
def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev   # new head
lst = SingleLinkedList()
for val in [1, 2, 3, 4]:
    lst.add_at_tail(val)

print("Original List:")
lst.display()

lst.head = reverse_linked_list(lst.head)
print("Reversed List:")
lst.display()