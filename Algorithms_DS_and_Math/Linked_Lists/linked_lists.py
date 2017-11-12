class Node:

    def __init__(self, value):
        self.next = None
        self.value = value


class DLLNode:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def cycle_check(node):
    marker1 = node
    marker2 = node

    while marker2 != None and marker2.next != None:

        marker1 = marker1.next
        marker2 = marker2.next.next

        if marker2 == marker1:
            return True

    return False

#Test Cycle Check

a = Node('a')
b = Node('b')
c = Node('c')

a.next = b
b.next = c
c.next = a

print(cycle_check(a))

a.next = b
b.next = c
c.next = None

print(cycle_check(a))

#Iterative Time O(n) Space O(1)
def reverse(head):
    current = head
    prev = None

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next

reverse(a)

print(c.next.value)
print(b.next.value)
print(a.next)

a = Node('a')
b = Node('b')
c = Node('c')

a.next = b
b.next = c
c.next = a
