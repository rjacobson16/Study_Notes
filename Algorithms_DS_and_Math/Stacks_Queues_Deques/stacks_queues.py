class Stack:

    def __init__(self):
        self.store = []

    def push(self, item):
        self.store.append(item)

    def pop(self):
        return self.store.pop()

    def peek(self):
        return self.store[-1]

    def isEmpty(self):
        return len(self.store) == 0

    def size(self):
        return len(self.store)

class Queue:

    def __init__(self):
        self.store = []

    def enqueue(self, item):
        self.store.append(item)

    def dequeue(self):
        return self.store.pop(0)

    def isEmpty(self):
        return len(self.store) == 0

    def size(self):
        return len(self.store)


class Deque:

    def __init__(self):
        self.store = []

    def addFront(self, item):
        self.store.insert(0, item)

    def addBack(self, item):
        self.store.append(item)

    def removeFront(self):
        return self.store.pop(0)

    def removeBack(self):
        return self.store.pop()

    def isEmpty(self):
        return len(self.store) == 0

    def size(self):
        return len(self.store)

## Interview Problems

def balanced_parens(string):
    left_brackets = {'{':'}', '[':']', '(':')'}
    s = Stack()

    for ch in string:
        if ch in left_brackets:
            s.push(ch)
        else:
            if left_brackets[s.peek()] == ch:
                s.pop()
            else:
                return False
    if not s.isEmpty():
         return False
    return True

class Queue2Stacks:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)
        print(self.stack1.store)
        print(self.stack2.store)

    def dequeue(self):
        if not self.stack2.isEmpty():
            return self.stack2.pop()
        elif not self.stack1.isEmpty():
            while True:
                if self.stack1.isEmpty():
                    break
                self.stack2.push(self.stack1.pop())
            return self.stack2.pop()
        else:
            return None

    def size(self):
        return self.stack1.size() + self.stack2.size()

    def isEmpty(self):
        return self.stack1.size() == 0 and self.stack2.size() == 0
