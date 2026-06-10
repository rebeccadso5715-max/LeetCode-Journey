# LeetCode #141 — Linked List Cycle

**Difficulty:** Easy

---

# Problem

Given the head of a linked list.

Determine whether the linked list contains a cycle.

Return:

```python
True
```

if a cycle exists.

Otherwise:

```python
False
```

---

## Example

### Input

```text
3 → 2 → 0 → -4
    ↑       ↓
    └───────┘
```

### Output

```python
True
```

### Explanation

The last node points back to a previous node.

Therefore:

```text
The list loops forever.
```

---

# What is a Cycle?

Normal Linked List:

```text
1 → 2 → 3 → 4 → null
```

Traversal ends.

---

Linked List with Cycle:

```text
1 → 2 → 3 → 4
    ↑       ↓
    └───────┘
```

Traversal never ends.

---

# Brute Force Approach (Hash Set)

Store every visited node.

If a node appears again:

```python
return True
```

---

## Python Solution

```python
class Solution:
    def hasCycle(self, head):

        visited = set()

        curr = head

        while curr:

            if curr in visited:
                return True

            visited.add(curr)

            curr = curr.next

        return False
```

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(n) |

### Why O(n) Space?

The set may store every node.

---

# Optimal Approach (Floyd's Cycle Detection)

Also called:

```text
Tortoise and Hare Algorithm
```

Use two pointers:

```text
slow → moves 1 step

fast → moves 2 steps
```

---

# Core Idea

If there is NO cycle:

```text
fast reaches null
```

---

If there IS a cycle:

```text
fast eventually catches slow
```

inside the loop.

---

# Visualization

Cycle:

```text
1 → 2 → 3 → 4
    ↑       ↓
    └───────┘
```

---

### Initial

```text
S,F

1 → 2 → 3 → 4
```

---

### Move

```text
slow → 2

fast → 3
```

---

### Move Again

```text
slow → 3

fast → 2
```

---

### Move Again

```text
slow → 4

fast → 4
```

Same node.

Cycle found.

---

# Why Must They Meet?

Imagine a circular running track.

```text
slow = 1 step

fast = 2 steps
```

The faster runner gains:

```text
1 step every iteration
```

Eventually:

```text
fast catches slow
```

Exactly the same idea.

---

# Python Solution

```python
class Solution:
    def hasCycle(self, head):

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next

            fast = fast.next.next

            if slow == fast:
                return True

        return False
```

---

# Dry Run

Input:

```text
3 → 2 → 0 → -4
    ↑       ↓
    └───────┘
```

---

### Initial

```python
slow = 3
fast = 3
```

---

### Iteration 1

```python
slow = 2

fast = 0
```

Not equal.

---

### Iteration 2

```python
slow = 0

fast = 2
```

Not equal.

---

### Iteration 3

```python
slow = -4

fast = -4
```

Equal.

Return:

```python
True
```

---

# Visualization

```text
Iteration 1

S
↓
3 → 2 → 0 → -4
          ↑    ↓
          └────┘

F
↓
0

----------------

Iteration 2

slow = 0

fast = 2

----------------

Iteration 3

slow = -4

fast = -4

Meet

Cycle Found
```

---

# What If There Is No Cycle?

Example:

```text
1 → 2 → 3 → null
```

Eventually:

```python
fast = None
```

or

```python
fast.next = None
```

Loop stops.

Return:

```python
False
```

---

# Why Check

```python
while fast and fast.next
```

?

Because:

```python
fast.next.next
```

must be safe.

Without this check:

```python
AttributeError
```

can occur.

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(1) |

### Why O(n)?

Every node is visited at most a few times.

---

### Why O(1)?

Only two pointers:

```python
slow
fast
```

are used.

No Hash Set.

---

# Java Solution

```java
public class Solution {

    public boolean hasCycle(
        ListNode head
    ) {

        ListNode slow = head;
        ListNode fast = head;

        while(fast != null &&
              fast.next != null) {

            slow = slow.next;

            fast = fast.next.next;

            if(slow == fast) {
                return true;
            }
        }

        return false;
    }
}
```

---

# Interview Insight

This problem introduces the most important Linked List technique:

```text
Fast & Slow Pointers
```

Also called:

```text
Tortoise and Hare
```

This pattern appears in:

- Middle Node
- Cycle Detection
- Happy Number
- Reorder List
- Find Duplicate Number

---

# Pattern Recognition

Whenever you hear:

- Cycle
- Loop
- Circular Structure
- Middle Node
- Fast and Slow

Think:

```text
Floyd's Algorithm
```

---

# Common Mistakes

## Mistake 1

Using:

```python
while fast:
```

instead of:

```python
while fast and fast.next
```

---

## Mistake 2

Comparing values:

```python
slow.val == fast.val
```

Wrong.

Compare nodes:

```python
slow == fast
```

---

## Mistake 3

Using extra memory unnecessarily.

Hash Set works.

Floyd's algorithm is better.

---

# Fast & Slow Pointer Cheat Sheet

```python
slow = head
fast = head

while fast and fast.next:

    slow = slow.next

    fast = fast.next.next

    if slow == fast:
        return True
```

Memorize this pattern.

---

# Key Takeaways

✅ A cycle means traversal never reaches null

✅ Hash Set solution works in O(n) space

✅ Floyd's algorithm uses O(1) space

✅ Slow moves 1 step

✅ Fast moves 2 steps

✅ If a cycle exists, they must meet

✅ One of the most important Linked List patterns

---

# Related Problems

1. Middle of the Linked List (#876)
2. Happy Number (#202)
3. Find the Duplicate Number (#287)
4. Linked List Cycle II (#142)
5. Reorder List (#143)

All use Fast & Slow Pointers.

---

# Golden Rule Learned

```text
Need To Detect A Cycle?
          ↓
Use Fast & Slow Pointers
```

Floyd's Cycle Detection Algorithm is one of the most elegant and frequently asked interview techniques.
