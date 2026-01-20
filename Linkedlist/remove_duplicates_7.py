from singlelist_1 import SingleLinkedList
def remove_duplicates(head):
    seen = set()
    temp = head
    prev = None
    while temp:
        if temp.data in seen:
            prev.next = temp.next
        else:
            seen.add(temp.data)
            prev = temp
        temp = temp.next
lst = SingleLinkedList()
for val in [10, 20, 30, 20, 40, 30]:
    lst.add_at_tail(val)

print("Before Removing Duplicates:")
lst.display()
remove_duplicates(lst.head)
print("After Removing Duplicates:")
lst.display()