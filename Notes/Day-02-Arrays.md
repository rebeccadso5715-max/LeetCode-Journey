# Arrays Fundamentals for Coding Interviews

## Why Arrays Matter

Before solving hard problems, you must become extremely comfortable with arrays.

### Why?

Because:

- Around 70% of interview problems are built on top of arrays.
- Arrays form the foundation of many important data structures and algorithms.
- Arrays + Hashing + Two Pointers + Sliding Window cover a huge portion of coding interview questions.

---

# What is an Array?

An array stores multiple values in contiguous memory locations.

### Example

```python
nums = [10, 20, 30, 40]
```

### Visualization

```text
Index:  0   1   2   3
Value: 10  20  30  40
```

### Accessing an Element

```python
nums[2]
```

Output:

```python
30
```

---

# Common Array Operations

## 1. Access

```python
nums[2]
```

### Time Complexity

```text
O(1)
```

Accessing any index takes constant time.

---

## 2. Update

```python
nums[2] = 100
```

### Time Complexity

```text
O(1)
```

Updating a value at a known index is instant.

---

## 3. Search

```python
for num in nums:
    if num == target:
        return True
```

### Time Complexity

```text
O(n)
```

In the worst case, every element must be checked.

---

## 4. Insert at End

```python
nums.append(50)
```

### Time Complexity

```text
O(1) Average
```

Appending is usually very efficient.

---

## 5. Insert at Beginning

```python
nums.insert(0, 50)
```

### Time Complexity

```text
O(n)
```

Why?

Because every existing element must shift one position to the right.

---

# Interview Rule #1

Whenever you see an array problem, immediately ask:

> Can I solve this in one pass?

Many optimized solutions aim to process the array only once.

Examples:

- Two Pointers
- Sliding Window
- Prefix Sum
- Hash Map Tracking

Reducing multiple passes to a single pass often improves performance from:

```text
O(n²) → O(n)
```

---

# Key Takeaways

✅ Arrays provide O(1) access.

✅ Searching is usually O(n).

✅ Appending is typically O(1).

✅ Inserting at the beginning is O(n).

✅ Most interview questions build upon array concepts.

✅ Always think: "Can I solve this in one pass?"

---

# Next Topics to Learn

1. Time Complexity (Big O)
2. Hashing
3. Prefix Sums
4. Two Pointers
5. Sliding Window
6. Binary Search
7. Stacks
8. Queues
9. Trees
10. Graphs

Master arrays first—everything else becomes much easier.
