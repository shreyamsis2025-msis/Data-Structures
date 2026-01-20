from singlelist_1 import SingleLinkedList
def common_elements(list1, list2):
    s1 = set()
    temp = list1.head
    while temp:
        s1.add(temp.data)
        temp = temp.next

    result = SingleLinkedList()
    temp = list2.head
    while temp:
        if temp.data in s1:
            result.add_at_tail(temp.data)
        temp = temp.next
    return result
l1 = SingleLinkedList()
l2 = SingleLinkedList()
for val in [1, 2, 3, 4]:
    l1.add_at_tail(val)
for val in [3, 4, 5, 6]:
    l2.add_at_tail(val)

print("List 1:")
l1.display()
print("List 2:")
l2.display()

common = common_elements(l1, l2)
print("Common Elements:")
common.display()