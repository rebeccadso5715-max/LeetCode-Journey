# LeetCode #100 — Same Tree

**Difficulty:** Easy

---

# Problem

Given two binary trees:

```python
p
q
```

Determine whether they are:

```text
Exactly The Same
```

Two trees are the same if:

1. Their structure is identical.
2. Their node values are identical.

---

## Example 1

### Input

```text
    1        1
   / \      / \
  2   3    2   3
```

### Output

```python
True
```

---

## Example 2

### Input

```text
    1        1
   /          \
  2            2
```

### Output

```python
False
```

Different structure.

---

## Example 3

### Input

```text
    1        1
   / \      / \
  2   1    1   2
```

### Output

```python
False
```

Different values.

---

# Key Observation

To determine if two trees are the same:

For every pair of nodes:

```text
Values must match

AND

Left subtrees must match

AND

Right subtrees must match
```

---

# Why Recursion Works

Each tree consists of:

```text
Root

Left Subtree

Right Subtree
```

To compare two trees:

```text
Compare Roots

Compare Left Subtrees

Compare Right Subtrees
```

This is the same problem repeated on smaller trees.

Perfect recursion.

---

# Recursive Strategy

At each node:

### Case 1

Both nodes are:

```text
None
```

Trees match.

Return:

```python
True
```

---

### Case 2

Only one node is:

```text
None
```

Trees differ.

Return:

```python
False
```

---

### Case 3

Values differ.

Return:

```python
False
```

---

### Case 4

Compare both subtrees.

---

# Python Solution

```python
class Solution:

    def isSameTree(self, p, q):

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return (
            self.isSameTree(
                p.left,
                q.left
            )
            and
            self.isSameTree(
                p.right,
                q.right
            )
        )
```

---

# Understanding the Code

## Both Empty

```python
if not p and not q:
```

Example:

```text
None     None
```

These match.

Return:

```python
True
```

---

## One Empty

```python
if not p or not q:
```

Example:

```text
None     5
```

Not equal.

Return:

```python
False
```

---

## Different Values

```python
if p.val != q.val:
```

Example:

```text
3     4
```

Not equal.

Return:

```python
False
```

---

## Compare Children

```python
left trees same

AND

right trees same
```

Both must be true.

---

# Dry Run

Tree A:

```text
      1
     / \
    2   3
```

Tree B:

```text
      1
     / \
    2   3
```

---

Compare:

```text
1 vs 1
```

Match.

---

Compare left:

```text
2 vs 2
```

Match.

---

Compare:

```text
None vs None
```

True.

---

Compare right:

```text
3 vs 3
```

Match.

---

Everything matches.

Return:

```python
True
```

---

# Visualization

```text
isSame(1,1)

├── isSame(2,2)
│
│   ├── isSame(None,None)
│   └── isSame(None,None)
│
└── isSame(3,3)

    ├── isSame(None,None)
    └── isSame(None,None)
```

Every comparison returns:

```text
True
```

Final answer:

```python
True
```

---

# Example of Failure

```text
      1
     /
    2
```

vs

```text
      1
       \
        2
```

---

Compare:

```text
Left

2 vs None
```

One exists.

One doesn't.

Return:

```python
False
```

Immediately.

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(h) |

---

## Why O(n)?

Every node is compared:

```text
Once
```

---

## Why O(h)?

Recursion stack stores:

```text
Tree Height
```

calls.

---

Worst case:

```text
Skewed Tree
```

Space:

```text
O(n)
```

---

Balanced tree:

```text
O(log n)
```

---

# Iterative Solution

Use a queue.

Compare nodes level by level.

---

## Python

```python
from collections import deque

class Solution:

    def isSameTree(self, p, q):

        queue = deque([(p, q)])

        while queue:

            n1, n2 = queue.popleft()

            if not n1 and not n2:
                continue

            if not n1 or not n2:
                return False

            if n1.val != n2.val:
                return False

            queue.append(
                (n1.left, n2.left)
            )

            queue.append(
                (n1.right, n2.right)
            )

        return True
```

---

# Java Solution

```java
class Solution {

    public boolean isSameTree(
        TreeNode p,
        TreeNode q
    ) {

        if(p == null &&
           q == null)
            return true;

        if(p == null ||
           q == null)
            return false;

        if(p.val != q.val)
            return false;

        return isSameTree(
                   p.left,
                   q.left
               )
               &&
               isSameTree(
                   p.right,
                   q.right
               );
    }
}
```

---

# Interview Insight

This problem teaches:

```text
Compare Two Trees
```

A very common pattern.

The rule:

```text
Compare Current Nodes

Then Compare Children
```

appears repeatedly.

---

# Pattern Recognition

Whenever you hear:

- Same Tree
- Identical Trees
- Equal Trees
- Compare Structures

Think:

```text
DFS Recursion
```

---

# Common Mistakes

## Mistake 1

Checking values before:

```python
None checks
```

May cause errors.

---

## Mistake 2

Using:

```python
or
```

instead of:

```python
and
```

Both subtrees must match.

---

## Mistake 3

Only comparing values.

Structure must also match.

---

# Tree Comparison Cheat Sheet

```python
Both None

→ True

One None

→ False

Values Different

→ False

Compare Left
AND
Compare Right
```

---

# Key Takeaways

✅ Trees must match in structure

✅ Trees must match in values

✅ Uses DFS recursion

✅ Compare left subtrees

✅ Compare right subtrees

✅ Time = O(n)

✅ Space = O(h)

---

# Related Problems

1. Symmetric Tree (#101)
2. Subtree of Another Tree (#572)
3. Invert Binary Tree (#226)
4. Balanced Binary Tree (#110)
5. Lowest Common Ancestor (#236)

All use DFS tree recursion.

---

# Golden Rule Learned

```text
Comparing Trees?
       ↓
Compare Roots
       ↓
Compare Left
       ↓
Compare Right
```

Same Tree is one of the cleanest examples of recursive tree comparison and a must-know interview problem.
