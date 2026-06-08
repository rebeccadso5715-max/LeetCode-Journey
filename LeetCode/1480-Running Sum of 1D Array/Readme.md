# LeetCode #1480 — Running Sum of 1D Array

**Difficulty:** Easy

---

## Problem

### Input

```python
[1, 2, 3, 4]
```

### Output

```python
[1, 3, 6, 10]
```

### Explanation

```text
1
1 + 2 = 3
1 + 2 + 3 = 6
1 + 2 + 3 + 4 = 10
```

---

# Brute Force Approach

For every index:

- Start from the beginning.
- Calculate the sum up to the current index.
- Store the result.

## Python Solution

```python
class Solution:
    def runningSum(self, nums):
        ans = []

        for i in range(len(nums)):
            total = 0

            for j in range(i + 1):
                total += nums[j]

            ans.append(total)

        return ans
```

---

## Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n²) |
| Space | O(n) |

Why O(n²)?

For every element, we iterate through all previous elements.

---

# Optimal Approach

Instead of recomputing the sum every time, reuse the previous answer.

Observation:

```text
runningSum[i]
=
runningSum[i-1] + nums[i]
```

---

## Python Solution

```python
class Solution:
    def runningSum(self, nums):

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        return nums
```

---

# Dry Run

Input:

```python
[1, 2, 3, 4]
```

### i = 1

```python
nums[1] += nums[0]

2 + 1 = 3

[1, 3, 3, 4]
```

### i = 2

```python
nums[2] += nums[1]

3 + 3 = 6

[1, 3, 6, 4]
```

### i = 3

```python
nums[3] += nums[2]

4 + 6 = 10

[1, 3, 6, 10]
```

Final Answer:

```python
[1, 3, 6, 10]
```

---

## Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(1) |

Why O(1) Space?

We modify the input array itself and do not create any extra array.

---

# Java Solution

```java
class Solution {

    public int[] runningSum(int[] nums) {

        for(int i = 1; i < nums.length; i++) {
            nums[i] += nums[i - 1];
        }

        return nums;
    }
}
```

---

# Interview Insight

Whenever you hear words like:

- Running Sum
- Prefix Sum
- Cumulative Sum
- Sum Till Index
- Range Sum Queries

Think immediately:

## Prefix Sum

Prefix Sum is one of the most important interview patterns.

Many medium and hard problems are built on top of this idea.

Examples:

- Running Sum of 1D Array
- Range Sum Query
- Subarray Sum Equals K
- Continuous Subarray Sum
- Product Except Self

---

# Key Takeaways

✅ Brute Force recalculates sums repeatedly → O(n²)

✅ Optimal solution reuses previous work → O(n)

✅ Running Sum is the simplest Prefix Sum problem

✅ Prefix Sum is a high-frequency interview pattern

✅ Always look for ways to reuse previous computations
