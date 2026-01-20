from singlelist_1 import SingleLinkedList

def split_alternate(head):
    list1 = SingleLinkedList()
    list2 = SingleLinkedList()
    temp = head
    toggle = True
    while temp:
        if toggle:
            list1.add_at_tail(temp.data)
        else:
            list2.add_at_tail(temp.data)
        toggle = not toggle
        temp = temp.next
    return list1, list2

lst = SingleLinkedList()
for val in [1, 2, 3, 4, 5, 6]:
    lst.add_at_tail(val)

print("Original List:")
lst.display()

l1, l2 = split_alternate(lst.head)
print("First Split List:")
l1.display()
print("Second Split List:")
l2.display()