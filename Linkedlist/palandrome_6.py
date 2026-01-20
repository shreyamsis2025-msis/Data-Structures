from singlelist_1 import SingleLinkedList
def is_palindrome(head):
    vals = []
    temp = head
    while temp:
        vals.append(temp.data)
        temp = temp.next
    return vals == vals[::-1]
lst = SingleLinkedList()
for val in [1, 2, 3, 2, 1]:
    lst.add_at_tail(val)

lst.display()
print("Is Palindrome?", is_palindrome(lst.head))