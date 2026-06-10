# Mental Model

Think of a Linked List as a treasure hunt.

Array:

```text
Index tells you exactly where to go.

nums[5]
```

Linked List:

```text
You must follow clues.

head
 ↓
1 → 2 → 3 → 4 → 5
```

To reach node 5:

```text
Start at head
Go to next
Go to next
Go to next
Go to next
```

There are no indices.

Only pointers.

---

# Common Mistakes

## Mistake 1

Forgetting to move forward.

Wrong:

```python
while current:

    print(current.val)
```

Infinite loop.

Correct:

```python
while current:

    print(current.val)

    current = current.next
```

---

## Mistake 2

Losing the next node.

Wrong:

```python
current.next = prev
current = current.next
```

You lost the original next node.

Always save:

```python
nxt = current.next
```

before changing pointers.

---

## Mistake 3

Not checking for null.

Wrong:

```python
print(head.next.val)
```

If:

```python
head = None
```

Error occurs.

Always handle edge cases.

---

# Fast & Slow Pointer Preview

One of the most important Linked List tricks.

```text
slow → moves 1 step

fast → moves 2 steps
```

Example:

```text
1 → 2 → 3 → 4 → 5

slow ends at 3
```

Applications:

- Middle Node
- Cycle Detection
- Happy Number
- Reorder List

---

# Dummy Node Preview

A fake node placed before the head.

Example:

```text
dummy → 1 → 2 → 3
```

Why?

It makes insertions and deletions near the head much easier.

Many interviewers expect this technique.

---

# Interview Pattern Recognition

Whenever you hear:

- Reverse
- Merge
- Cycle
- Middle
- Remove Node
- Reorder

Think:

```text
Linked List
+
Pointer Manipulation
```

---

# Linked List Cheat Sheet

| Pattern | Used For |
|----------|-----------|
| Traversal | Visit all nodes |
| Reverse | Reverse Linked List |
| Fast & Slow | Middle Node, Cycle Detection |
| Dummy Node | Easy insertion/deletion |
| Merge | Sorted Lists |
| Two Pointers | Remove Nth Node |

---

# Final Takeaway

Arrays are:

```text
Index Based
```

Linked Lists are:

```text
Pointer Based
```

Success in Linked List problems comes from understanding:

```text
How pointers move
```

not from memorizing code.

---

# Golden Rule

```text
Need Fast Insert/Delete
At The Front?
        ↓
Use Linked List
```

Linked Lists trade fast random access for fast pointer manipulation.
