# LeetCode #21 — Merge Two Sorted Lists

**Difficulty:** Easy

---

# Problem

You are given the heads of two sorted linked lists.

Merge them into one sorted linked list.

Return the head of the merged list.

---

## Example

### Input

```text
List 1:

1 → 2 → 4

List 2:

1 → 3 → 4
```

### Output

```text
1 → 1 → 2 → 3 → 4 → 4
```

---

# Key Observation

Both lists are already:

```text
Sorted
```

This means:

At every step:

```text
Take the smaller node.
```

Very similar to:

```text
Merge step of Merge Sort
```

---

# Brute Force Approach

1. Copy all values into an array.
2. Sort the array.
3. Create a new linked list.

---

## Complexity

| Metric | Complexity |
|----------|------------|
| Time | O((n+m) log(n+m)) |
| Space | O(n+m) |

Not optimal.

---

# Optimal Approach

Use:

```text
Two Pointers
```

One pointer for each list.

```text
list1
list2
```

Create a dummy node.

```text
dummy → ?
```

Build the answer from there.

---

# Why Dummy Node?

Without a dummy node:

```text
Need special handling
for the first node.
```

With dummy:

```text
Always attach to tail.
```

Much cleaner.

---

# Visualization

Initial:

```text
dummy

↓

0

List1

1 → 2 → 4

List2

1 → 3 → 4
```

---

# Python Solution

```python
class Solution:
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode()
        tail = dummy

        while list1 and list2:

            if list1.val < list2.val:

                tail.next = list1
                list1 = list1.next

            else:

                tail.next = list2
                list2 = list2.next

            tail = tail.next

        tail.next = list1 or list2

        return dummy.next
```

---

# Dry Run

Input:

```text
1 → 2 → 4

1 → 3 → 4
```

---

### Step 1

Compare:

```text
1 vs 1
```

Take second list's node.

```text
dummy → 1
```

Move:

```python
list2 = list2.next
```

---

### Step 2

Compare:

```text
1 vs 3
```

Take first list node.

```text
dummy → 1 → 1
```

Move:

```python
list1 = list1.next
```

---

### Step 3

Compare:

```text
2 vs 3
```

Take:

```text
2
```

Result:

```text
1 → 1 → 2
```

---

### Step 4

Compare:

```text
4 vs 3
```

Take:

```text
3
```

Result:

```text
1 → 1 → 2 → 3
```

---

### Step 5

Compare:

```text
4 vs 4
```

Take one of them.

Result:

```text
1 → 1 → 2 → 3 → 4
```

---

One list ends.

Attach remaining nodes.

Final:

```text
1 → 1 → 2 → 3 → 4 → 4
```

---

# Full Visualization

```text
List1

1 → 2 → 4

List2

1 → 3 → 4

----------------

Take 1

Merged

1

----------------

Take 1

Merged

1 → 1

----------------

Take 2

Merged

1 → 1 → 2

----------------

Take 3

Merged

1 → 1 → 2 → 3

----------------

Take 4

Merged

1 → 1 → 2 → 3 → 4

----------------

Attach Remaining

1 → 1 → 2 → 3 → 4 → 4
```

---

# Understanding

```python
tail.next = list1
```

means:

```text
Attach current node
to merged list.
```

---

```python
tail = tail.next
```

means:

```text
Move tail forward.
```

---

```python
tail.next = list1 or list2
```

means:

```text
One list is finished.

Attach whatever remains.
```

---

# Why Does This Work?

Because both lists are sorted.

The smallest remaining node must be:

```text
list1.val
or
list2.val
```

No other node can be smaller.

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n + m) |
| Space | O(1) |

Where:

```text
n = length of list1
m = length of list2
```

---

### Why O(n+m)?

Every node is visited exactly once.

---

### Why O(1)?

No extra data structures.

Only pointers:

```python
dummy
tail
list1
list2
```

---

# Java Solution

```java
class Solution {

    public ListNode mergeTwoLists(
        ListNode list1,
        ListNode list2
    ) {

        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;

        while(list1 != null &&
              list2 != null) {

            if(list1.val < list2.val) {

                tail.next = list1;
                list1 = list1.next;
            }

            else {

                tail.next = list2;
                list2 = list2.next;
            }

            tail = tail.next;
        }

        tail.next =
            (list1 != null) ? list1 : list2;

        return dummy.next;
    }
}
```

---

# Interview Insight

This problem introduces the:

```text
Dummy Node Pattern
```

which appears everywhere in Linked Lists.

Examples:

- Remove Nth Node
- Partition List
- Swap Nodes in Pairs
- Reverse Nodes in K Groups

---

# Pattern Recognition

Whenever you hear:

- Merge Lists
- Build New List
- Insert At Head
- Insert At Beginning

Think:

```text
Dummy Node
```

---

# Common Mistakes

## Mistake 1

Returning:

```python
dummy
```

Instead of:

```python
dummy.next
```

---

## Mistake 2

Forgetting:

```python
tail = tail.next
```

after attaching a node.

---

## Mistake 3

Forgetting to attach remaining nodes.

Wrong:

```python
while list1 and list2:
```

and then immediately return.

You lose leftover nodes.

Always:

```python
tail.next = list1 or list2
```

---

# Dummy Node Cheat Sheet

```python
dummy = ListNode()

tail = dummy

tail.next = node

tail = tail.next

return dummy.next
```

Memorize this pattern.

---

# Key Takeaways

✅ Lists are already sorted

✅ Compare current nodes

✅ Take smaller node

✅ Use dummy node

✅ Move tail forward

✅ Attach remaining nodes

✅ O(n+m) time

✅ O(1) space

---

# Related Problems

1. Merge K Sorted Lists (#23)
2. Sort List (#148)
3. Partition List (#86)
4. Swap Nodes in Pairs (#24)
5. Reverse Nodes in K Group (#25)

These all use dummy nodes heavily.

---

# Golden Rule Learned

```text
Building A New Linked List?
            ↓
      Use Dummy Node
```

The Dummy Node Pattern is one of the most important Linked List tricks in coding interviews.
