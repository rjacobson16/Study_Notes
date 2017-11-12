# Linked Lists

## Singly Linked Lists

  * A singly linked lists is a collection of nodes that forms a linear sequence
  * Each node carries a pointer to the following node
  * Each list has a member named head and (in some implementations) a member named tail
  * Tail can be identified by None as next


### Inserting at the Head of a SLL

  * Linked lists do not have a fixed size
  * To insert at the head:
    * Create a new node
    * Set its element to the new element
    * Set its 'next' ling to refer to the current head
    * Then set the list's head to point to the new node

  * Removing from head simply reverse of insertion, but efficient deletion from end
  requires *doubly linked list*

## Linked List Pros

Pros:
  * Constant time insertion and deletion
  * Can expand without having to specify size, unlike array

Cons
  * Accessing takes O(k) time - from head to kth element, unlike array

## Doubly Linked Lists

  * In a DLL, each node keeps a reference to the node before AND after it
  * Greater variety of O(1) time operations

## Sentinel Node
  * We add special dummy nodes at both ends of the list.
  * A header and a trailer, called *sentinels*

## Deletion
  * Two neighbors of the node are linked directly to each other
  * As a result, that node will not be considered part of the list
  * Sentinels allow the same implementation when deleting the first or
  last element
