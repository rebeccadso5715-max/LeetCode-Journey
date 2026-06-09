# Hashing Fundamentals for Coding Interviews

## Why Hashing Matters

If Arrays are the foundation, Hashing is the superpower.

Many O(n²) solutions become O(n) because of hashing.

---

# What is Hashing?

A hash table stores data in the form:

```text
Key → Value
```

---

## Python Example

```python
student = {
    "Rebecca": 100,
    "John": 95
}
```

Accessing a value:

```python
print(student["Rebecca"])
```

Output:

```text
100
```

---

## Java Example

```java
HashMap<String, Integer> map = new HashMap<>();

map.put("Rebecca", 100);
map.put("John", 95);
```

---

# Why Do We Use Hashing?

Without hashing, searching requires scanning the array.

```python
nums = [10, 20, 30, 40]

target = 30

for num in nums:
    if num == target:
        return True
```

### Complexity

```text
O(n)
```

Because we may need to check every element.

---

# Using Hashing

Convert the data into a set:

```python
seen = {10, 20, 30, 40}

30 in seen
```

Output:

```text
True
```

### Complexity

```text
O(1) Average Case
```

Hash tables allow direct access instead of scanning.

---

# Most Important Operations

## Insert

```python
mp = {}

mp[5] = 100
```

### Complexity

```text
O(1)
```

---

## Search

```python
5 in mp
```

### Complexity

```text
O(1)
```

---

## Delete

```python
del mp[5]
```

### Complexity

```text
O(1)
```

---

# Hash Set vs Hash Map

## Hash Set

Stores only values.

```python
seen = {1, 2, 3, 4}
```

Questions it answers:

```text
Is x present?
```

Example:

```python
3 in seen
```

---

## Hash Map

Stores key-value pairs.

```python
freq = {
    1: 3,
    2: 5
}
```

Questions it answers:

```text
What information is associated with x?
```

Example:

```python
freq[1]
```

Output:

```text
3
```

---

# Interview Pattern Recognition

Whenever you hear:

- Find duplicates
- Check if an element exists
- Count frequencies
- Two Sum
- Longest Substring Without Repeating Characters
- Top K Frequent Elements

Think:

```text
Hash Set
or
Hash Map
```

---

# Example: Find Duplicates

Without hashing:

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            return True
```

### Complexity

```text
O(n²)
```

---

With hashing:

```python
seen = set()

for num in nums:

    if num in seen:
        return True

    seen.add(num)

return False
```

### Complexity

```text
O(n)
```

---

# Example: Frequency Counting

Input:

```python
nums = [1, 1, 2, 3, 3, 3]
```

Code:

```python
freq = {}

for num in nums:

    if num not in freq:
        freq[num] = 0

    freq[num] += 1

print(freq)
```

Output:

```python
{
    1: 2,
    2: 1,
    3: 3
}
```

---

# Complexity Summary

| Operation | Average Complexity |
|------------|------------------|
| Insert | O(1) |
| Search | O(1) |
| Delete | O(1) |

---

# Important Interview Insight

Hashing trades:

```text
Extra Memory
        ↓
Faster Lookup
```

Most interview optimizations follow this pattern:

```text
O(n²)
   ↓
O(n)
```

by storing previously seen information in a hash table.

---

# Key Takeaways

✅ Hashing provides fast lookups

✅ Hash Set stores values only

✅ Hash Map stores key-value pairs

✅ Insert, Search, Delete are O(1) average

✅ Frequently used in interview problems

✅ Hashing often converts O(n²) solutions into O(n)

---

# Next Problems to Practice

1. Two Sum
2. Contains Duplicate
3. Valid Anagram
4. Intersection of Two Arrays
5. Top K Frequent Elements
6. Group Anagrams

Master these and you'll understand the core hashing patterns used in coding interviews.
