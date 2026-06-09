# Class 5 — Sliding Window

## Why Sliding Window Matters

Sliding Window is one of the most powerful interview patterns.

It is essentially an optimized version of:

```text
Two Pointers
```

Many problems that would normally require:

```text
O(n²)
```

can be solved in:

```text
O(n)
```

using Sliding Window.

---

# Biggest Clues

Whenever you see words like:

- Subarray
- Substring
- Contiguous
- Longest
- Shortest
- Maximum Length
- Minimum Length
- Consecutive Elements

Think:

```text
Sliding Window
```

---

# What is a Sliding Window?

Instead of generating every possible subarray:

```python
for i in range(n):
    for j in range(i, n):
        ...
```

Maintain a window:

```python
left = 0
right = 0
```

Visualization:

```text
Array

[1, 2, 3, 4, 5]

 L
 R
```

Expand:

```python
right += 1
```

Shrink:

```python
left += 1
```

---

# Why Is It Faster?

Brute Force:

```text
Generate every subarray
```

Complexity:

```text
O(n²)
```

---

Sliding Window:

Each pointer moves at most:

```text
n times
```

Complexity:

```text
O(n)
```

---

# Window Visualization

Array:

```python
[1, 2, 3, 4, 5]
```

Window:

```text
[1]
```

Expand:

```text
[1,2]
```

Expand:

```text
[1,2,3]
```

Shrink:

```text
[2,3]
```

Expand:

```text
[2,3,4]
```

Expand:

```text
[2,3,4,5]
```

The window continuously moves across the array.

---

# General Template

```python
left = 0

for right in range(len(nums)):

    # Expand window

    while window_is_invalid:

        # Shrink window
        left += 1

    # Update answer
```

This template solves many interview questions.

---

# Types of Sliding Window

## 1. Fixed Size Window

Window size never changes.

Example:

```text
Find maximum sum of any
subarray of size k.
```

Window:

```text
Size = 3

[1,2,3]
  [2,3,4]
    [3,4,5]
```

---

### Fixed Window Template

```python
window_sum = 0
k = 3

for i in range(len(nums)):

    window_sum += nums[i]

    if i >= k:
        window_sum -= nums[i-k]

    if i >= k-1:
        answer = max(answer, window_sum)
```

---

# Example

Input:

```python
nums = [1,2,3,4,5]
k = 3
```

Windows:

```text
[1,2,3] = 6
[2,3,4] = 9
[3,4,5] = 12
```

Answer:

```python
12
```

---

## 2. Variable Size Window

Window expands and shrinks dynamically.

Examples:

- Longest Substring Without Repeating Characters
- Minimum Size Subarray Sum
- Fruit Into Baskets

---

### Variable Window Template

```python
left = 0

for right in range(len(nums)):

    add(nums[right])

    while invalid_window:

        remove(nums[left])
        left += 1

    answer = max(answer,
                 right - left + 1)
```

---

# Example

Problem:

```text
Longest substring
without repeating characters
```

Input:

```python
"abcabcbb"
```

Window:

```text
abc
```

Next:

```text
abca
```

Invalid because:

```text
a repeated
```

Shrink:

```text
bca
```

Continue...

Maximum length:

```python
3
```

---

# Fixed vs Variable Window

| Type | Window Size |
|--------|------------|
| Fixed | Constant |
| Variable | Changes Dynamically |

---

## Fixed Window Clues

When you hear:

```text
Size K
Exactly K
Window Length K
```

Think:

```text
Fixed Sliding Window
```

---

## Variable Window Clues

When you hear:

```text
Longest
Shortest
At Most K
At Least K
Without Repeating
Distinct Characters
```

Think:

```text
Variable Sliding Window
```

---

# Relationship with Two Pointers

Sliding Window is simply:

```text
Two Pointers
+
Window Maintenance
```

Pointers:

```text
left -> -> right
```

Unlike normal Two Pointers:

```text
left ->      <- right
```

both pointers move in the same direction.

---

# Complexity Analysis

## Brute Force

```text
O(n²)
```

Generate every subarray.

---

## Sliding Window

```text
O(n)
```

Because:

```text
left moves at most n times
right moves at most n times
```

Total:

```text
2n = O(n)
```

---

# Interview Pattern Recognition

Whenever you hear:

- Subarray
- Substring
- Contiguous
- Longest
- Shortest
- Maximum Length
- Minimum Length

Think:

```text
Sliding Window
```

---

# Key Takeaways

✅ Sliding Window is an optimized Two Pointer technique

✅ Used for subarrays and substrings

✅ Avoids generating every possible window

✅ Often reduces O(n²) → O(n)

✅ Two major types:
- Fixed Size Window
- Variable Size Window

✅ One of the most frequently tested interview patterns

---

# Problems We'll Solve Next

### Fixed Window

1. Maximum Average Subarray I (#643)

---

### Variable Window

2. Longest Substring Without Repeating Characters (#3)

3. Minimum Size Subarray Sum (#209)

4. Longest Repeating Character Replacement (#424)

5. Permutation in String (#567)

6. Minimum Window Substring (#76)

---

# Golden Rule Learned

```text
Subarray / Substring
        +
Longest / Shortest
        ↓
Think Sliding Window
```

Master Sliding Window and you'll unlock a huge category of medium and hard interview questions.
