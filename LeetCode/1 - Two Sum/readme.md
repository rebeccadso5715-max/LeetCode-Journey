# LeetCode #1 — Two Sum

**Difficulty:** Easy

---

# Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

You may assume that:

- Exactly one valid answer exists.
- You may not use the same element twice.

---

## Example

### Input

```python
nums = [2, 7, 11, 15]
target = 9
```

### Output

```python
[0, 1]
```

### Explanation

```text
nums[0] + nums[1]
=
2 + 7
=
9
```

Therefore:

```python
[0, 1]
```

---

# Brute Force Approach

Check every possible pair.

For each element:

- Compare it with all elements after it.
- If their sum equals the target, return the indices.

---

## Python Solution

```python
class Solution:
    def twoSum(self, nums, target):

        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):

                if nums[i] + nums[j] == target:
                    return [i, j]
```

---

# Dry Run

Input:

```python
nums = [2, 7, 11, 15]
target = 9
```

### i = 0

```python
j = 1

2 + 7 = 9
```

Found answer:

```python
[0, 1]
```

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n²) |
| Space | O(1) |

### Why O(n²)?

Nested loops:

```text
n × n
=
O(n²)
```

---

# Optimal Approach (Hash Map)

Instead of checking every pair:

Store previously seen numbers in a hash map.

For each number:

```text
need = target - current_number
```

Check:

```text
Have we already seen "need"?
```

If yes:

```text
need + current_number = target
```

Answer found.

---

## Python Solution

```python
class Solution:
    def twoSum(self, nums, target):

        seen = {}

        for i, num in enumerate(nums):

            need = target - num

            if need in seen:
                return [seen[need], i]

            seen[num] = i
```

---

# Dry Run

Input:

```python
nums = [2, 7, 11, 15]
target = 9
```

Initially:

```python
seen = {}
```

---

### Iteration 1

```python
num = 2
need = 9 - 2
need = 7
```

Check:

```python
7 in seen ?
```

No.

Store:

```python
seen = {
    2: 0
}
```

---

### Iteration 2

```python
num = 7
need = 9 - 7
need = 2
```

Check:

```python
2 in seen ?
```

Yes ✅

```python
seen[2] = 0
```

Answer:

```python
[0, 1]
```

---

# Visualization

```text
Target = 9

Index  Number

0      2
       Need = 7
       Store 2 → 0

1      7
       Need = 2
       Found 2 in HashMap

Answer = [0, 1]
```

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(n) |

### Why O(n)?

We traverse the array once.

Hash map lookup is O(1) average.

### Why O(n) Space?

In the worst case, all numbers may be stored.

---

# Java Solution

```java
import java.util.HashMap;

class Solution {

    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> seen = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {

            int need = target - nums[i];

            if(seen.containsKey(need)) {
                return new int[]{
                    seen.get(need),
                    i
                };
            }

            seen.put(nums[i], i);
        }

        return new int[]{};
    }
}
```

---

# Interview Insight

This is the most famous Hash Map problem.

The key idea:

```text
Instead of searching the future,
store the past.
```

For every number:

```text
Ask:
What number do I need
to reach the target?
```

Then check if that number has already been seen.

---

# Pattern Recognition

Whenever you hear:

- Find a pair
- Find two numbers
- Target sum
- Complement
- Lookup previous value

Think:

```text
Hash Map
```

---

# Key Takeaways

✅ Brute Force checks every pair → O(n²)

✅ Hash Map stores previously seen numbers

✅ Lookup becomes O(1) average

✅ Overall complexity improves to O(n)

✅ One of the most important interview patterns

---

# Related Problems

1. Contains Duplicate
2. Two Sum II
3. 3Sum
4. 4Sum
5. Subarray Sum Equals K
6. Top K Frequent Elements
7. Longest Consecutive Sequence

Master Two Sum and you'll start recognizing Hash Map patterns everywhere.
