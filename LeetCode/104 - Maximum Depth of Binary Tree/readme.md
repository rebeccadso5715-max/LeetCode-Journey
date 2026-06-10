# LeetCode #104 — Maximum Depth of Binary Tree

**Difficulty:** Easy

---

# Problem

Given the root of a binary tree:

Return:

```text
Maximum Depth
```

of the tree.

The depth is:

```text
Number of nodes
along the longest path
from root to leaf.
```

---

## Example

Tree:

```text
        3
      /   \
     9     20
          /  \
         15   7
```

Output:

```python
3
```

Because the longest path is:

```text
3 → 20 → 15
```

or

```text
3 → 20 → 7
```

which contains:

```text
3 nodes
```

---

# Key Observation

To find the depth of a tree:

```text
Find depth of left subtree

Find depth of right subtree

Take maximum
```

Then:

```text
Add 1 for current node
```

---

# Recursive Formula

Let:

```text
depth(node)
```

represent maximum depth of a tree rooted at:

```text
node
```

Then:

```text
depth(node)

=

1 + max(
        depth(left),
        depth(right)
      )
```

---

# Why Recursion Works

Every subtree is itself a tree.

Example:

```text
        1
       / \
      2   3
```

To compute:

```text
depth(1)
```

we first compute:

```text
depth(2)

depth(3)
```

Smaller versions of the same problem.

Perfect recursion.

---

# Python Solution

```python
class Solution:

    def maxDepth(self, root):

        if not root:
            return 0

        return 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
        )
```

---

# Understanding the Code

## Base Case

```python
if not root:
    return 0
```

An empty tree has depth:

```text
0
```

---

## Recursive Step

```python
maxDepth(left)
```

returns:

```text
Depth of left subtree
```

---

```python
maxDepth(right)
```

returns:

```text
Depth of right subtree
```

---

Take:

```python
max(...)
```

because we want:

```text
Longest Path
```

---

Add:

```python
1
```

for the current node.

---

# Dry Run

Tree:

```text
      1
     / \
    2   3
```

---

Compute:

```text
depth(1)
```

---

Need:

```text
depth(2)

depth(3)
```

---

For:

```text
depth(2)
```

Children are:

```text
None
None
```

So:

```text
1 + max(0,0)

=

1
```

---

Similarly:

```text
depth(3)

=

1
```

---

Root:

```text
1 + max(1,1)

=

2
```

Answer:

```python
2
```

---

# Visualization

```text
          1
         / \
        2   3
       /
      4
```

---

Node:

```text
4
```

Depth:

```text
1
```

---

Node:

```text
2
```

Depth:

```text
1 + max(1,0)

=

2
```

---

Node:

```text
3
```

Depth:

```text
1
```

---

Node:

```text
1
```

Depth:

```text
1 + max(2,1)

=

3
```

---

# Recursion Tree

```text
maxDepth(1)

├── maxDepth(2)
│   └── maxDepth(4)
│
└── maxDepth(3)
```

Each call returns its depth upward.

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(h) |

---

## Why O(n)?

Every node is visited:

```text
Exactly Once
```

---

## Why O(h)?

Recursion stack stores:

```text
Height of Tree
```

calls.

---

Worst case:

```text
1
 \
  2
   \
    3
     \
      4
```

Height:

```text
n
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

space.

---

# Iterative Solution (DFS Stack)

## Python

```python
class Solution:

    def maxDepth(self, root):

        if not root:
            return 0

        stack = [(root, 1)]

        depth = 0

        while stack:

            node, level = stack.pop()

            depth = max(
                depth,
                level
            )

            if node.left:
                stack.append(
                    (node.left,
                     level + 1)
                )

            if node.right:
                stack.append(
                    (node.right,
                     level + 1)
                )

        return depth
```

---

# Java Solution

```java
class Solution {

    public int maxDepth(
        TreeNode root
    ) {

        if(root == null)
            return 0;

        return 1 + Math.max(
            maxDepth(root.left),
            maxDepth(root.right)
        );
    }
}
```

---

# Interview Insight

This is one of the most important beginner tree problems.

It teaches:

```text
Tree Recursion
```

The pattern:

```text
Answer At Node

=

Function(Left)

+

Function(Right)
```

appears everywhere.

---

# Pattern Recognition

Whenever you hear:

- Height
- Depth
- Longest Path
- Tree Height
- Maximum Level

Think:

```text
DFS
+
Recursion
```

---

# Common Mistakes

## Mistake 1

Returning:

```python
1
```

for null node.

Correct:

```python
0
```

---

## Mistake 2

Using:

```python
min(...)
```

instead of:

```python
max(...)
```

We want longest path.

---

## Mistake 3

Forgetting:

```python
+1
```

for current node.

---

# Tree Recursion Cheat Sheet

```python
if not root:
    return 0

return 1 + max(
    left_answer,
    right_answer
)
```

---

# Key Takeaways

✅ Maximum depth = longest root-to-leaf path

✅ Uses DFS recursion

✅ Every subtree is a smaller tree

✅ Recurrence:

```text
1 + max(left,right)
```

✅ Time = O(n)

✅ Space = O(h)

✅ One of the most important tree interview questions

---

# Related Problems

1. Same Tree (#100)
2. Balanced Binary Tree (#110)
3. Diameter of Binary Tree (#543)
4. Minimum Depth of Binary Tree (#111)
5. Invert Binary Tree (#226)

All use DFS recursion.

---

# Golden Rule Learned

```text
Need Tree Height
Or Maximum Depth?
        ↓
DFS
        ↓
1 + max(left,right)
```

Maximum Depth is often the first problem that teaches the fundamental recursion pattern used throughout tree-based interviews.
