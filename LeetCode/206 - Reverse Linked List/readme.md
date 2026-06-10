# LeetCode #206 — Reverse Linked List

**Difficulty:** Easy

---

# Problem

Given the head of a singly linked list.

Reverse the list and return the new head.

---

## Example

### Input

```text
1 → 2 → 3 → 4 → 5 → null
```

### Output

```text
5 → 4 → 3 → 2 → 1 → null
```

---

# Key Observation

Each node currently points:

```text
Forward
```

Example:

```text
1 → 2 → 3
```

We need:

```text
1 ← 2 ← 3
```

The challenge is:

```text
Don't lose the next node
while reversing pointers.
```

---

# Visualization

Initial:

```text
prev    curr
 ↓       ↓

null ← 1 → 2 → 3 → 4 → 5
```

Goal:

```text
5 → 4 → 3 → 2 → 1 → null
```

---

# Core Idea

At every step:

### Step 1

Save next node.

```python
nxt = curr.next
```

---

### Step 2

Reverse pointer.

```python
curr.next = prev
```

---

### Step 3

Move prev forward.

```python
prev = curr
```

---

### Step 4

Move curr forward.

```python
curr = nxt
```

Repeat until:

```python
curr = None
```

---

# Python Solution

```python
class Solution:
    def reverseList(self, head):

        prev = None
        curr = head

        while curr:

            nxt = curr.next

            curr.next = prev

            prev = curr

            curr = nxt

        return prev
```

---

# Dry Run

Input:

```text
1 → 2 → 3 → null
```

---

### Initial State

```text
prev = null

curr = 1
```

---

### Iteration 1

Save:

```python
nxt = 2
```

Reverse:

```text
1 → null
```

Move:

```python
prev = 1
curr = 2
```

---

Current List:

```text
null ← 1

2 → 3
```

---

### Iteration 2

Save:

```python
nxt = 3
```

Reverse:

```text
2 → 1 → null
```

Move:

```python
prev = 2
curr = 3
```

---

### Iteration 3

Save:

```python
nxt = null
```

Reverse:

```text
3 → 2 → 1 → null
```

Move:

```python
prev = 3
curr = null
```

Loop ends.

Return:

```python
prev
```

---

# Full Visualization

```text
Initial

null ← 1 → 2 → 3 → 4 → 5

--------------------

After First Iteration

null ← 1

2 → 3 → 4 → 5

--------------------

After Second Iteration

null ← 1 ← 2

3 → 4 → 5

--------------------

After Third Iteration

null ← 1 ← 2 ← 3

4 → 5

--------------------

Final

5 → 4 → 3 → 2 → 1 → null
```

---

# Why Do We Need `nxt`?

Without:

```python
nxt = curr.next
```

we lose access to the rest of the list.

Example:

Before:

```text
1 → 2 → 3
```

If we immediately do:

```python
curr.next = prev
```

Result:

```text
1 → null
```

Now:

```text
2 → 3
```

is lost forever.

That's why saving:

```python
nxt
```

is mandatory.

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(1) |

### Why O(n)?

Every node is visited exactly once.

---

### Why O(1)?

Only three pointers:

```python
prev
curr
nxt
```

are used.

---

# Java Solution

```java
class Solution {

    public ListNode reverseList(
        ListNode head
    ) {

        ListNode prev = null;
        ListNode curr = head;

        while(curr != null) {

            ListNode nxt = curr.next;

            curr.next = prev;

            prev = curr;

            curr = nxt;
        }

        return prev;
    }
}
```

---

# Interview Insight

This is the most important Linked List problem.

Nearly every advanced Linked List question uses this logic.

Examples:

- Reverse Linked List II
- Palindrome Linked List
- Reorder List
- Reverse Nodes in K Groups

---

# Pattern Recognition

Whenever you hear:

- Reverse List
- Reverse Portion
- Reverse Between
- Reverse Every K Nodes

Think:

```text
Pointer Reversal
```

---

# Common Mistakes

## Mistake 1

Forgetting:

```python
nxt = curr.next
```

before reversing.

This loses the list.

---

## Mistake 2

Returning:

```python
head
```

Instead of:

```python
prev
```

After reversal:

```text
prev
```

becomes the new head.

---

## Mistake 3

Moving pointers in the wrong order.

Always:

```python
Save Next

Reverse

Move Prev

Move Curr
```

---

# Reverse Linked List Cheat Sheet

```python
nxt = curr.next

curr.next = prev

prev = curr

curr = nxt
```

Memorize these four lines.

They appear repeatedly in Linked List interviews.

---

# Key Takeaways

✅ Reverse pointers one by one

✅ Save next node before changing pointers

✅ Use:

- prev
- curr
- nxt

✅ Return `prev`

✅ O(n) time

✅ O(1) space

✅ Most important Linked List problem

---

# Related Problems

1. Reverse Linked List II (#92)
2. Palindrome Linked List (#234)
3. Reorder List (#143)
4. Reverse Nodes in K Group (#25)
5. Swap Nodes in Pairs (#24)

All build directly on this reversal technique.

---

# Golden Rule Learned

```text
Before Changing Pointer
         ↓
Save Next Node
```

This single rule prevents the most common Linked List bug and is the foundation of pointer manipulation problems.
