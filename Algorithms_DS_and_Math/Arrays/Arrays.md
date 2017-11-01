# Array Sequences

Python has 3 main sequence classes - all support indexing
  * List [1,2,3]
  * Tuple (1,2,3)
  * String '123'

## Low Level Arrays

* Memory of computer stored in bits, 8 bits in a byte

* Each byte has a corresponding *memory address* Contiguous bytes have consecutive memory addresses

* Programming language keeps track of assoc. between identifier
and memory address

* Python - unicode character = 2 bytes

* Each cell of an array must use same amt of bytes for constant time access

## Referential Array

* Since each cell in the array must use the same number of bytes, we store *references*
to objects in the array. Each reference is the same size, even if the objects vary.

* `new_arr = list(arr)` makes a shallow copy of the arr. If object reference is mutable, make a deep copy

## Dynamic Array

* Automatically resizes when capacity reached
