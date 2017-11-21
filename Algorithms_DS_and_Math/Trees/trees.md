# Trees

* We'll implement trees with lists as well as classes. We'll implement priority queue.

### About

* Data structure w/ root, branches, and leaves

* data structure has root at top and leaves at bottom

* Example: biological classification tree, file tree (directories)

### Node

* Fundamental part of a tree. Can have name, called 'key'

* Node may have additional info called 'payload'

* Payload not central to many algorithms, but oft critical in apps

### Edge

  * Connects 2 nodes
  * each node (besides root) is connected by exactly one incoming edge
  * each node may have several outgoing

### Path

  * Ordered list of nodes connected by edges

### Children

  * a set of nodes that have incoming edges from the same node  

### Parent

  * a node is the parent of all nodes it connects to with outgoing edges

### Sibling

  * children of same parent

### Subtree

  * set of nodes and edges comprised of a parent and all descendants

### Leaf

  * Node with no children

### Level

  * level of a node 'n' is the number of edges on the path from root to n

### Height

  * maximum level of any node in the tree


------

* If each node has a max of 2 children, then the tree is a binary tree

### Recursive definition of tree

  * Tree either empty or consists of a root and 0 or more subtrees, each also being a tree

  * Root of each subtree connected by root of parent tree by an edge

## Implementation

  * [Implementation](Algorithms_DS_and_Math/Trees/trees.py)

### List of lists

  * store value of root node as first element of list
  * second el of list is a list representing the left subtree

  * third el is a list that represents the right subtree
