# Class 6 — Binary Search

## Why Binary Search Matters

Binary Search is one of the highest-frequency interview topics.

Many interview problems that appear difficult are actually variations of Binary Search.

It is one of the most important techniques to master.

---

# Biggest Clues

Whenever you see:

- Sorted Array
- Search
- Minimum
- Maximum
- Answer Space
- First Occurrence
- Last Occurrence
- Rotated Array

Think:

```text
Binary Search
```

---

# What is Binary Search?

Instead of checking every element one by one:

```text
O(n)
```

we repeatedly cut the search space in half.

---

# Example

Suppose:

```python
nums = [1,2,3,4,5,6,7,8]
```

Target:

```python
7
```

Linear Search:

```text
1 → 2 → 3 → 4 → 5 → 6 → 7
```

Worst Case:

```text
O(n)
```

---

Binary Search:

```text
1 2 3 4 5 6 7 8

Middle = 4

Target > 4

Discard Left Half

5 6 7 8

Middle = 6

Target > 6

Discard Left Half

7 8

Middle = 7

Found
```

---

# Why Is It Fast?

Each step removes half the remaining elements.

Example:

```text
100 Elements

100
↓
50
↓
25
↓
12
↓
6
↓
3
↓
1
```

Number of operations:

```text
log₂(100)
≈ 7
```

Instead of:

```text
100
```

---

# Complexity

| Algorithm | Time |
|------------|--------|
| Linear Search | O(n) |
| Binary Search | O(log n) |

---

# Requirement

Binary Search usually requires:

```text
Sorted Data
```

Without sorting:

```text
Binary Search does not work.
```

---

# Binary Search Template

```python
left = 0
right = len(nums) - 1

while left <= right:

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid

    elif nums[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

return -1
```

---

# Understanding the Variables

### Left Pointer

```python
left
```

Start of search space.

---

### Right Pointer

```python
right
```

End of search space.

---

### Mid Pointer

```python
mid = (left + right) // 2
```

Middle element.

---

# Visualization

Array:

```python
[1,2,3,4,5,6,7,8,9]
```

Target:

```python
7
```

Initial:

```text
L       M       R

1 2 3 4 5 6 7 8 9
        ↑
```

---

### Step 1

```python
mid = 4
value = 5
```

Target:

```python
7
```

Since:

```python
7 > 5
```

Discard left half.

```python
left = mid + 1
```

---

### Step 2

Search Space:

```text
6 7 8 9
```

Middle:

```python
7
```

Found.

---

# Dry Run

Input:

```python
nums = [1,3,5,7,9]
target = 7
```

---

### Iteration 1

```python
left = 0
right = 4

mid = 2
nums[mid] = 5
```

Since:

```python
7 > 5
```

Move:

```python
left = 3
```

---

### Iteration 2

```python
left = 3
right = 4

mid = 3
nums[mid] = 7
```

Found.

Return:

```python
3
```

---

# Why Does It Work?

Because the array is sorted.

If:

```python
nums[mid] < target
```

everything left of mid is also smaller.

So we can safely discard:

```text
Entire Left Half
```

---

If:

```python
nums[mid] > target
```

everything right of mid is also larger.

Discard:

```text
Entire Right Half
```

---

# Common Binary Search Variations

## 1. Search Target

Example:

```text
Binary Search (#704)
```

---

## 2. First Occurrence

Example:

```text
Find First Position
```

---

## 3. Last Occurrence

Example:

```text
Find Last Position
```

---

## 4. Rotated Sorted Array

Example:

```text
Search in Rotated Sorted Array (#33)
```

---

## 5. Answer Space Binary Search

Example:

```text
Koko Eating Bananas (#875)
```

Search the answer itself.

---

# Common Mistakes

## Mistake 1

Using:

```python
while left < right
```

when template requires:

```python
while left <= right
```

---

## Mistake 2

Forgetting:

```python
mid + 1
```

or

```python
mid - 1
```

which causes infinite loops.

---

## Mistake 3

Using Binary Search on:

```text
Unsorted Arrays
```

---

# Pattern Recognition

Whenever you hear:

- Sorted Array
- Search
- First Position
- Last Position
- Rotated Array
- Minimum Possible
- Maximum Possible

Think:

```text
Binary Search
```

---

# Complexity Analysis

| Operation | Complexity |
|------------|------------|
| Search | O(log n) |
| Space | O(1) |

---

# Key Takeaways

✅ Binary Search requires sorted data

✅ Repeatedly divide search space by 2

✅ Much faster than Linear Search

✅ Complexity is O(log n)

✅ One of the most important interview topics

✅ Foundation for many medium and hard problems

---

# Problems We'll Solve Next

### Basic Binary Search

1. Binary Search (#704)

### Boundaries

2. First Bad Version (#278)

3. Search Insert Position (#35)

### Rotated Arrays

4. Search in Rotated Sorted Array (#33)

5. Find Minimum in Rotated Sorted Array (#153)

### Answer Space Binary Search

6. Koko Eating Bananas (#875)

7. Capacity To Ship Packages Within D Days (#1011)

---

# Golden Rule Learned

```text
Sorted Array
     +
Search
     ↓
Binary Search
```

Master Binary Search and you'll unlock a huge category of medium and hard interview problems.
