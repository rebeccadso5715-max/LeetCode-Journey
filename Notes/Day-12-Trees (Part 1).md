# Class 12 — Trees (Part 1)

## Why Trees Matter

Trees are one of the highest-frequency topics in coding interviews.

Many advanced topics are built on trees:

- Binary Trees
- Binary Search Trees (BST)
- Heaps
- Tries
- Segment Trees
- Decision Trees

A huge number of interview questions are solved using:

```text
DFS

or

BFS
```

on trees.

---

# What is a Tree?

Think of a tree as:

```text
A Linked List
That Can Branch
```

Instead of:

```text
1 → 2 → 3 → 4
```

we can have:

```text
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
```

Each node can connect to multiple children.

---

# Real World Examples

## File System

```text
Documents
├── Notes
├── PDFs
└── Projects
```

---

## Organization Chart

```text
CEO
├── Manager A
└── Manager B
```

---

## HTML DOM

```html
<html>
    <body>
        <div>
```

Tree structure.

---

# Tree Terminology

Consider:

```text
        1
      /   \
     2     3
    / \
   4   5
```

---

## Root

Top node.

```text
        1
```

Root:

```text
1
```

---

## Parent

Node above another node.

Example:

```text
1
```

is parent of:

```text
2 and 3
```

---

## Child

Node below another node.

Example:

```text
2
```

is child of:

```text
1
```

---

## Siblings

Nodes with same parent.

Example:

```text
2 and 3
```

---

## Leaf Node

Node with no children.

Example:

```text
4
5
3
```

---

## Edge

Connection between nodes.

```text
1 ── 2
```

One edge.

---

## Height

Longest path from node to a leaf.

Example:

```text
        1
       /
      2
     /
    3
```

Height of root:

```text
2
```

(edges)

---

## Depth

Distance from root.

Example:

```text
Depth(1)=0

Depth(2)=1

Depth(3)=2
```

---

# Binary Tree

A Binary Tree is a tree where every node has:

```text
At Most Two Children
```

Called:

```text
Left Child

Right Child
```

Example:

```text
      1
     / \
    2   3
```

---

# Binary Tree Node

## Python

```python
class TreeNode:

    def __init__(
        self,
        val=0,
        left=None,
        right=None
    ):

        self.val = val
        self.left = left
        self.right = right
```

---

## Java

```java
class TreeNode {

    int val;

    TreeNode left;

    TreeNode right;

    TreeNode(int val) {

        this.val = val;
    }
}
```

---

# Creating a Tree

## Python

```python
root = TreeNode(1)

root.left = TreeNode(2)

root.right = TreeNode(3)
```

Tree:

```text
      1
     / \
    2   3
```

---

# Tree Traversal

Traversal means:

```text
Visit Every Node
```

Trees are usually traversed using:

```text
DFS

or

BFS
```

---

# DFS Traversals

DFS means:

```text
Depth First Search
```

Go deep before exploring siblings.

---

Consider:

```text
        1
      /   \
     2     3
    / \   / \
   4  5  6  7
```

---

# 1. Preorder Traversal

Rule:

```text
Root

Left

Right
```

---

## Pattern

```text
Root → Left → Right
```

---

### Visualization

```text
Visit 1

Visit 2

Visit 4

Visit 5

Visit 3

Visit 6

Visit 7
```

Output:

```text
1 2 4 5 3 6 7
```

---

## Python

```python
def preorder(root):

    if not root:
        return

    print(root.val)

    preorder(root.left)

    preorder(root.right)
```

---

# 2. Inorder Traversal

Rule:

```text
Left

Root

Right
```

---

## Pattern

```text
Left → Root → Right
```

---

### Visualization

```text
4

2

5

1

6

3

7
```

Output:

```text
4 2 5 1 6 3 7
```

---

## Python

```python
def inorder(root):

    if not root:
        return

    inorder(root.left)

    print(root.val)

    inorder(root.right)
```

---

# 3. Postorder Traversal

Rule:

```text
Left

Right

Root
```

---

## Pattern

```text
Left → Right → Root
```

---

### Visualization

```text
4

5

2

6

7

3

1
```

Output:

```text
4 5 2 6 7 3 1
```

---

## Python

```python
def postorder(root):

    if not root:
        return

    postorder(root.left)

    postorder(root.right)

    print(root.val)
```

---

# Easy Example

Tree:

```text
      1
     / \
    2   3
```

---

## Preorder

```text
1 2 3
```

---

## Inorder

```text
2 1 3
```

---

## Postorder

```text
2 3 1
```

---

# DFS Memory Trick

## Preorder

```text
Root First
```

---

## Inorder

```text
Root Middle
```

---

## Postorder

```text
Root Last
```

---

# Complexity

For all DFS traversals:

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(h) |

Where:

```text
h = tree height
```

---

# Why Recursion Works So Well?

A tree is naturally recursive.

Every subtree is itself:

```text
A Smaller Tree
```

Example:

```text
        1
       / \
      2   3
```

Node:

```text
2
```

is also a tree.

Node:

```text
3
```

is also a tree.

---

# Common Interview Clues

Whenever you hear:

- Root
- Left Child
- Right Child
- Leaf
- Subtree
- Height
- Depth

Think:

```text
Tree
```

---

# Problems We'll Solve Next

### Easy

1. Maximum Depth of Binary Tree (#104)

2. Same Tree (#100)

3. Invert Binary Tree (#226)

---

### Medium

4. Binary Tree Level Order Traversal (#102)

5. Validate BST (#98)

6. Lowest Common Ancestor (#236)

---

# Key Takeaways

✅ Trees are hierarchical structures

✅ Binary Trees have at most two children

✅ DFS has three traversals:

- Preorder
- Inorder
- Postorder

✅ Trees are naturally recursive

✅ DFS traversal is O(n)

✅ Foundation of many interview questions

---

# Golden Rule Learned

```text
Tree Problem?
     ↓
Think Recursion
     ↓
DFS
```

Most beginner tree problems can be solved by recursively processing the left subtree and right subtree.
