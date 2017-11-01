import ctypes

# Dynamic (auto-resizing) Array, like Python list or Ruby array

'''
Outline:

To resize, we need to

1. Allocate new arr (B) with greater capacity
2. copy all items from A to B
3. reassign A to B
'''
class Dynamic_Array:

    def __init__ (self):
        self.count = 0
        self.capacity = 1
        self.store = [None] *self.capacity

    def len(self):
        return self.count

    def __getitem__(self, i):

        if not 0 <= i < self.count:
            return (IndexError('index is out of bounds'))

        return self.store[i]

    def append(self, el):

        if self.count == self.capacity:
            self._resize

        self.store[self.count] = el

        self.count += 1

    def _resize(self):
        '''
            Simulates having to resize by increasing the capacity and
            copying elements into a new array in O(n) time.
        '''
        self.capacity *=2

        new_store = [None] *self.capacity

        for el in store:
            store += el

        self.store = new_store
