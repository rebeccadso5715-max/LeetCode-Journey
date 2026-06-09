# LeetCode #217 — Contains Duplicate

**Difficulty:** Easy

---

# Problem

Given an integer array `nums`, return:

```text
True
```

if any value appears at least twice in the array.

Otherwise return:

```text
False
```

---

## Example 1

### Input

```python
nums = [1, 2, 3, 1]
```

### Output

```python
True
```

### Explanation

```text
1 appears twice.
```

---

## Example 2

### Input

```python
nums = [1, 2, 3, 4]
```

### Output

```python
False
```

### Explanation

```text
All elements are unique.
```

---

# Brute Force Approach

Compare every pair of elements.

If any two elements are equal:

```python
return True
```

Otherwise:

```python
return False
```

---

## Python Solution

```python
class Solution:
    def containsDuplicate(self, nums):

        n = len(nums)

        for i in range(n):

            for j in range(i + 1, n):

                if nums[i] == nums[j]:
                    return True

        return False
```

---

# Dry Run

Input:

```python
[1, 2, 3, 1]
```

### i = 0

```python
Compare:

1 vs 2
1 vs 3
1 vs 1
```

Duplicate found ✅

Return:

```python
True
```

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n²) |
| Space | O(1) |

### Why O(n²)?

Nested loops compare every pair.

---

# Optimal Approach (Hash Set)

Use a Hash Set to remember previously seen numbers.

For each number:

1. Check if it already exists in the set.
2. If yes → duplicate found.
3. Otherwise add it to the set.

---

## Python Solution

```python
class Solution:
    def containsDuplicate(self, nums):

        seen = set()

        for num in nums:

            if num in seen:
                return True

            seen.add(num)

        return False
```

---

# Dry Run

Input:

```python
nums = [1, 2, 3, 1]
```

Initially:

```python
seen = {}
```

---

### num = 1

```python
1 in seen ?
```

No.

Add:

```python
seen = {1}
```

---

### num = 2

```python
2 in seen ?
```

No.

Add:

```python
seen = {1, 2}
```

---

### num = 3

```python
3 in seen ?
```

No.

Add:

```python
seen = {1, 2, 3}
```

---

### num = 1

```python
1 in seen ?
```

Yes ✅

Return:

```python
True
```

---

# Visualization

```text
Number   Seen Set

1        {1}

2        {1,2}

3        {1,2,3}

1        Already Exists
         ↓
       True
```

---

# Alternative One-Liner

```python
class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
```

### Why Does This Work?

Input:

```python
[1, 2, 3, 1]
```

Set removes duplicates:

```python
{1, 2, 3}
```

Lengths:

```python
len(nums) = 4
len(set(nums)) = 3
```

Different lengths ⇒ Duplicate exists.

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(n) |

### Why O(n)?

We traverse the array once.

Hash Set lookup is O(1) average.

### Why O(n) Space?

In the worst case, all elements are unique and stored.

---

# Java Solution

```java
import java.util.HashSet;

class Solution {

    public boolean containsDuplicate(int[] nums) {

        HashSet<Integer> seen = new HashSet<>();

        for(int num : nums) {

            if(seen.contains(num)) {
                return true;
            }

            seen.add(num);
        }

        return false;
    }
}
```

---

# Interview Insight

This problem teaches the most important use of a Hash Set:

```text
Fast Membership Checking
```

Instead of searching through the entire array every time:

```text
Store what you've already seen.
```

---

# Pattern Recognition

Whenever you hear:

- Contains Duplicate
- Seen Before
- Repeated Element
- Unique Elements
- Membership Check

Think:

```text
Hash Set
```

---

# Key Takeaways

✅ Brute Force compares every pair → O(n²)

✅ Hash Set provides O(1) average lookup

✅ Store previously seen values

✅ Overall complexity becomes O(n)

✅ One of the most common Hash Set interview patterns

---

# Related Problems

1. Two Sum
2. Valid Anagram
3. Intersection of Two Arrays
4. Happy Number
5. Longest Consecutive Sequence
6. Top K Frequent Elements

All of these heavily use Hash Sets or Hash Maps.
