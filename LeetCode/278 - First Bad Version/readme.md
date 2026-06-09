# LeetCode #278 — First Bad Version

**Difficulty:** Easy

---

# Problem

Suppose you are a product manager.

Versions are released as:

```text
1 → 2 → 3 → 4 → 5 → ... → n
```

At some point, a version becomes bad.

After that:

```text
All later versions are also bad.
```

Example:

```text
Version

1  2  3  4  5
G  G  B  B  B
```

(`G = Good`, `B = Bad`)

You are given an API:

```python
isBadVersion(version)
```

Return:

```text
The first bad version
```

---

## Example

### Input

```text
n = 5
firstBad = 4
```

Versions:

```text
1  2  3  4  5
G  G  G  B  B
```

### Output

```python
4
```

---

# Key Observation

We are NOT searching for:

```text
An exact value
```

Instead we are searching for:

```text
The first position
where a condition becomes true.
```

This is a classic:

```text
Binary Search on Boundary
```

problem.

---

# Visualization

Imagine:

```text
False False False True True True
```

or

```text
Good Good Good Bad Bad Bad
```

We need the:

```text
First True
```

or

```text
First Bad
```

---

# Brute Force Approach

Check versions one by one.

```python
for version in range(1, n + 1):

    if isBadVersion(version):
        return version
```

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(1) |

Too slow.

---

# Optimal Approach (Binary Search)

Use:

```python
left = 1
right = n
```

---

# Main Idea

If:

```python
isBadVersion(mid)
```

is True:

```text
mid might be the first bad version
```

So:

```python
right = mid
```

Notice:

```python
NOT right = mid - 1
```

because we cannot discard `mid`.

It might be the answer.

---

If:

```python
isBadVersion(mid)
```

is False:

```text
First bad version
must be after mid.
```

Move:

```python
left = mid + 1
```

---

# Python Solution

```python
class Solution:
    def firstBadVersion(self, n):

        left = 1
        right = n

        while left < right:

            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid

            else:
                left = mid + 1

        return left
```

---

# Dry Run

Input:

```text
n = 5

Versions:

1  2  3  4  5
G  G  G  B  B
```

---

### Iteration 1

```python
left = 1
right = 5

mid = 3
```

```python
isBadVersion(3)
```

Result:

```python
False
```

Move:

```python
left = 4
```

---

### Iteration 2

```python
left = 4
right = 5

mid = 4
```

```python
isBadVersion(4)
```

Result:

```python
True
```

Move:

```python
right = 4
```

---

Now:

```python
left = 4
right = 4
```

Loop ends.

Return:

```python
4
```

---

# Visualization

```text
1  2  3  4  5
G  G  G  B  B

mid = 3

Good

Discard Left Side

----------------

4  5
↑  ↑

mid = 4

Bad

Keep 4

right = 4

----------------

left = right = 4

Answer Found
```

---

# Why Use `while left < right`?

Notice:

```python
right = mid
```

instead of:

```python
right = mid - 1
```

Because of this:

```python
left <= right
```

can create infinite loops.

The safer boundary-search template is:

```python
while left < right
```

---

# Binary Search Templates

## 1. Exact Search

Used in:

```text
Binary Search (#704)
```

Template:

```python
while left <= right
```

---

## 2. First Occurrence

Used in:

```text
First Bad Version (#278)
```

Template:

```python
while left < right
```

---

## 3. Last Occurrence

Used in:

```text
Find Last Position
```

Boundary Binary Search.

---

## 4. Search Insert Position

Used in:

```text
Search Insert Position (#35)
```

Return:

```python
left
```

after Binary Search finishes.

---

## 5. Binary Search on Answer

Used in:

```text
Koko Eating Bananas (#875)
Capacity To Ship Packages (#1011)
```

Search the answer itself rather than an array index.

---

# Common Mistakes

## Mistake 1 — Wrong Loop Condition

Many beginners confuse:

```python
while left < right
```

and

```python
while left <= right
```

### Rule

**Exact Search**

```python
while left <= right
```

---

**Boundary Search**

```python
while left < right
```

---

## Mistake 2 — Infinite Loop

Wrong:

```python
left = mid
```

or

```python
right = mid
```

without understanding the template.

Always make progress.

For Exact Search:

```python
left = mid + 1
right = mid - 1
```

---

For First Bad Version:

```python
right = mid
left = mid + 1
```

This guarantees convergence.

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(log n) |
| Space | O(1) |

### Why O(log n)?

Each step removes half the remaining versions.

---

### Why O(1) Space?

Only:

```python
left
right
mid
```

are used.

---

# Java Solution

```java
public class Solution extends VersionControl {

    public int firstBadVersion(int n) {

        int left = 1;
        int right = n;

        while(left < right) {

            int mid =
                left + (right - left) / 2;

            if(isBadVersion(mid)) {
                right = mid;
            }

            else {
                left = mid + 1;
            }
        }

        return left;
    }
}
```

---

# Interview Insight

This problem teaches the most important Binary Search upgrade:

```text
Searching for a Boundary
```

Instead of finding:

```text
A Target
```

we find:

```text
The First Position
that satisfies a condition.
```

---

# Pattern Recognition

Whenever you hear:

- First Occurrence
- First True
- First Bad
- Lower Bound
- Earliest Valid Position

Think:

```text
Boundary Binary Search
```

---

# Key Takeaways

✅ Array doesn't need to be explicitly given

✅ Search space is versions `1 → n`

✅ Find the first position where condition becomes true

✅ Use `while left < right`

✅ Keep `mid` when it could be the answer

✅ O(log n) time

✅ O(1) space

---

# Related Problems

1. Binary Search (#704)
2. Search Insert Position (#35)
3. Find First and Last Position (#34)
4. Koko Eating Bananas (#875)
5. Capacity To Ship Packages Within D Days (#1011)

These all build on Binary Search boundary concepts.

---

# Golden Rule Learned

```text
Find First Position
Satisfying Condition
          ↓
Boundary Binary Search
```

First Bad Version is the classic introduction to **First Occurrence Binary Search**, one of the most important interview patterns.
