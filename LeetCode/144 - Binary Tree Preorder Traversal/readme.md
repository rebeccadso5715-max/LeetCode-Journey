# LeetCode #144 — Binary Tree Preorder Traversal

**Difficulty:** Easy

---

# Problem

Given the root of a binary tree:

Return its:

```text
Preorder Traversal
```

---

# What is Preorder Traversal?

Rule:

```text
Root
 ↓
Left
 ↓
Right
```

Memory Trick:

```text
Preorder

Root First
```

---

## Example

Tree:

```text
      1
     / \
    2   3
```

Traversal:

```text
Visit 1

Visit 2

Visit 3
```

Output:

```python
[1,2,3]
```

---

# Visualization

Tree:

```text
        1
      /   \
     2     3
    / \   / \
   4  5  6  7
```

Preorder:

```text
1

2

4

5

3

6

7
```

Output:

```python
[1,2,4,5,3,6,7]
```

---

# Why Recursion Works?

Every subtree is itself a tree.

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

is a smaller tree.

Node:

```text
3
```

is a smaller tree.

Therefore:

```text
Process Root

Process Left Subtree

Process Right Subtree
```

Recursively.

---

# Recursive DFS Solution

## Python

```python
class Solution:

    def preorderTraversal(self, root):

        result = []

        def dfs(node):

            if not node:
                return

            result.append(node.val)

            dfs(node.left)

            dfs(node.right)

        dfs(root)

        return result
```

---

# Understanding the Code

## Base Case

```python
if not node:
    return
```

Reached beyond a leaf.

Stop recursion.

---

## Visit Root

```python
result.append(node.val)
```

Preorder visits:

```text
Root First
```

---

## Traverse Left

```python
dfs(node.left)
```

---

## Traverse Right

```python
dfs(node.right)
```

---

# Dry Run

Tree:

```text
      1
     / \
    2   3
```

---

### dfs(1)

Add:

```python
[1]
```

---

### dfs(2)

Add:

```python
[1,2]
```

---

### dfs(None)

Return.

---

### dfs(None)

Return.

---

### dfs(3)

Add:

```python
[1,2,3]
```

---

Answer:

```python
[1,2,3]
```

---

# Recursion Visualization

```text
dfs(1)

│
├── dfs(2)
│
│   ├── dfs(None)
│   └── dfs(None)
│
└── dfs(3)

    ├── dfs(None)
    └── dfs(None)
```

---

# Iterative Solution (Stack)

Trees can also be traversed without recursion.

Use:

```text
Stack
```

Because DFS naturally uses a stack.

---

## Python

```python
class Solution:

    def preorderTraversal(self, root):

        if not root:
            return []

        stack = [root]

        result = []

        while stack:

            node = stack.pop()

            result.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return result
```

---

# Why Push Right First?

Stack is:

```text
LIFO
```

We want:

```text
Root → Left → Right
```

So:

```text
Push Right

Push Left
```

Then Left is processed first.

---

# Iterative Dry Run

Tree:

```text
      1
     / \
    2   3
```

Stack:

```text
[1]
```

---

Pop:

```text
1
```

Answer:

```text
[1]
```

Push:

```text
3
2
```

---

Pop:

```text
2
```

Answer:

```text
[1,2]
```

---

Pop:

```text
3
```

Answer:

```text
[1,2,3]
```

---

# Complexity Analysis

## Recursive DFS

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(h) |

Where:

```text
h = tree height
```

---

## Why O(n)?

Every node visited:

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

# Java Solution

```java
class Solution {

    List<Integer> result =
        new ArrayList<>();

    public List<Integer>
        preorderTraversal(
            TreeNode root
        ) {

        dfs(root);

        return result;
    }

    private void dfs(
        TreeNode node
    ) {

        if(node == null)
            return;

        result.add(node.val);

        dfs(node.left);

        dfs(node.right);
    }
}
```

---

# Interview Insight

Preorder traversal is commonly used when:

```text
Root must be processed first.
```

Examples:

- Copy Tree
- Serialize Tree
- Expression Trees
- Prefix Notation

---

# DFS Traversal Cheat Sheet

## Preorder

```text
Root

Left

Right
```

---

## Inorder

```text
Left

Root

Right
```

---

## Postorder

```text
Left

Right

Root
```

---

# Common Mistakes

## Mistake 1

Forgetting base case.

```python
if not node:
```

causes recursion to stop.

---

## Mistake 2

Wrong traversal order.

Preorder must be:

```python
Root

Left

Right
```

---

## Mistake 3

Using:

```python
dfs(left)

dfs(right)

append(root)
```

That's Postorder.

---

# Key Takeaways

✅ Preorder = Root → Left → Right

✅ Uses DFS

✅ Naturally solved using recursion

✅ Every node visited once

✅ Time = O(n)

✅ Space = O(h)

✅ One of the three fundamental DFS traversals

---

# Related Problems

1. Binary Tree Inorder Traversal (#94)
2. Binary Tree Postorder Traversal (#145)
3. Maximum Depth of Binary Tree (#104)
4. Same Tree (#100)
5. Invert Binary Tree (#226)

All build DFS tree intuition.

---

# Golden Rule Learned

```text
Need To Process
Root First?
      ↓
Use Preorder DFS
```

Preorder traversal is the foundation of many tree problems and is usually the first DFS traversal learned in interviews.
