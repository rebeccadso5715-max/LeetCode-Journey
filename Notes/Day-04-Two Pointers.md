# Class 4 — Two Pointers

## Why Two Pointers Matter

Two Pointers is one of the most common coding interview patterns.

Many problems that look like:

```text
O(n²)
```

can often be optimized to:

```text
O(n)
```

using Two Pointers.

---

# Biggest Clues

When you see words like:

- Array
- Sorted Array
- Pair
- Palindrome
- Reverse
- Two Ends
- Subarray
- Consecutive Elements

Think:

```text
Two Pointers
```

---

# What is the Two Pointer Technique?

Instead of using one index:

```python
i
```

Use two pointers:

```python
left = 0
right = len(nums) - 1
```

Move them according to the problem's conditions.

---

# Example

Array:

```python
nums = [2, 7, 11, 15]
```

Pointers:

```text
2   7   11   15
↑            ↑
L            R
```

The pointers can move:

```text
L → right
R → left
```

until a condition is satisfied.

---

# Why Use Two Pointers?

Without Two Pointers:

```python
for i in range(n):
    for j in range(i + 1, n):
        ...
```

Complexity:

```text
O(n²)
```

---

With Two Pointers:

```python
left = 0
right = n - 1

while left < right:
    ...
```

Complexity:

```text
O(n)
```

Much faster for large inputs.

---

# Three Major Two Pointer Patterns

## 1. Opposite Direction

```text
left  ->      <-  right
```

Pointers start at opposite ends and move inward.

### Used In

- Two Sum II
- Reverse String
- Valid Palindrome
- Container With Most Water
- 3Sum

### Example

```python
left = 0
right = len(nums) - 1

while left < right:

    if condition:
        left += 1

    else:
        right -= 1
```

---

## 2. Same Direction (Fast & Slow)

```text
slow -> -> fast
```

Both pointers move in the same direction.

Usually:

- Fast explores.
- Slow tracks useful positions.

### Used In

- Remove Duplicates
- Move Zeroes
- Linked List Cycle
- Remove Elements

### Example

```python
slow = 0

for fast in range(len(nums)):

    if nums[fast] != 0:
        nums[slow] = nums[fast]
        slow += 1
```

---

## 3. Sliding Window

```text
left -> -> right
```

Maintain a window.

Expand:

```python
right += 1
```

Shrink:

```python
left += 1
```

### Used In

- Longest Substring Without Repeating Characters
- Maximum Sum Subarray
- Minimum Window Substring
- Permutation in String

---

# Pattern 1 Example: Reverse String

Input:

```python
["h", "e", "l", "l", "o"]
```

Code:

```python
left = 0
right = len(s) - 1

while left < right:

    s[left], s[right] = s[right], s[left]

    left += 1
    right -= 1
```

Visualization:

```text
h  e  l  l  o
↑           ↑

Swap

o  e  l  l  h
   ↑     ↑

Swap

o  l  l  e  h
```

---

# Pattern 2 Example: Move Zeroes

Input:

```python
[0, 1, 0, 3, 12]
```

Output:

```python
[1, 3, 12, 0, 0]
```

Fast pointer finds non-zero values.

Slow pointer places them correctly.

---

# Pattern 3 Example: Sliding Window

Input:

```python
[1, 2, 3, 4]
```

Window:

```text
[1]
[1,2]
[1,2,3]
[2,3]
[2,3,4]
```

Window grows and shrinks dynamically.

---

# When Should You Think Two Pointers?

## Opposite Direction

When you hear:

```text
Pair
Sorted Array
Palindrome
Reverse
Two Ends
```

Think:

```text
Two Pointers
```

---

## Same Direction

When you hear:

```text
Remove
Move
Compress
Rearrange
```

Think:

```text
Fast & Slow Pointers
```

---

## Sliding Window

When you hear:

```text
Longest
Shortest
Maximum
Minimum
Substring
Subarray
```

Think:

```text
Sliding Window
```

---

# Complexity Benefits

| Approach | Time |
|-----------|--------|
| Nested Loops | O(n²) |
| Two Pointers | O(n) |

This optimization appears constantly in interviews.

---

# Key Takeaways

✅ Two Pointers is a high-frequency interview pattern

✅ Often converts O(n²) → O(n)

✅ Works especially well on sorted arrays

✅ Great for palindrome and reverse problems

✅ Foundation of Sliding Window

✅ Three major types:
- Opposite Direction
- Same Direction (Fast & Slow)
- Sliding Window

---

# Problems Covered So Far

### Opposite Direction

- Two Sum II (#167)
- Reverse String (#344)
- Valid Palindrome (#125)

### Coming Next

- Move Zeroes (#283)
- Remove Duplicates from Sorted Array (#26)
- Container With Most Water (#11)
- 3Sum (#15)
- Longest Substring Without Repeating Characters (#3)

Master these and you'll start recognizing Two Pointer patterns instantly.
