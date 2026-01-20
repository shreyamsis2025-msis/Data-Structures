from singlelist_1 import SingleLinkedList
def sum_last_n_nodes(head, n):
    fast = slow = head
    for _ in range(n):
        if fast:
            fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    total = 0
    while slow:
        total += slow.data
        slow = slow.next
    return total

#example usage
lst = SingleLinkedList()
for val in [10, 20, 30, 40, 50]:
    lst.add_at_tail(val)

print("List:")
lst.display()
print("Sum of last 3 nodes:", sum_last_n_nodes(lst.head, 3))