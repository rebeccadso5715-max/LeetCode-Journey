# Day 1 - Big O Analysis

## What is Big O?

Big O measures how the runtime or memory usage of an algorithm grows as the input size grows.

---

## Complexity Ranking

```text
O(1)
O(log n)
O(n)
O(n log n)
O(n²)
O(n³)
O(2ⁿ)
O(n!)
```

---

## O(1) - Constant Time

```python
arr = [10,20,30]
print(arr[1])
```

Time Complexity: O(1)

---

## O(n) - Linear Time

```python
for num in arr:
    print(num)
```

Time Complexity: O(n)

---

## O(n²) - Quadratic Time

```python
for i in arr:
    for j in arr:
        print(i, j)
```

Time Complexity: O(n²)

---

## O(log n)

Algorithms that repeatedly divide the search space by 2.

Example:

- Binary Search

Time Complexity: O(log n)

---

## O(n log n)

Common in efficient sorting algorithms:

- Merge Sort
- Heap Sort

Time Complexity: O(n log n)

---

## Key Learnings

- Big O measures growth, not actual execution time.
- O(log n) usually means halving.
- Nested loops often indicate O(n²).
- Output size can create a lower bound on runtime.
