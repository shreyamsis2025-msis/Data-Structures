from singlelist_1 import SingleLinkedList
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data if slow else None
lst = SingleLinkedList()
for val in [1, 2, 3, 4, 5]:
    lst.add_at_tail(val)

lst.display()
print("Middle Element:", find_middle(lst.head))