# LeetCode #643 — Maximum Average Subarray I

**Difficulty:** Easy

---

# Problem

Given an integer array `nums` consisting of `n` elements and an integer `k`.

Find the contiguous subarray of length `k` that has the maximum average value.

Return that average.

---

## Example

### Input

```python
nums = [1, 12, -5, -6, 50, 3]
k = 4
```

### Output

```python
12.75
```

### Explanation

Subarrays of size 4:

```text
[1, 12, -5, -6]  = 2
[12, -5, -6, 50] = 51
[-5, -6, 50, 3]  = 42
```

Maximum sum:

```text
51
```

Average:

```text
51 / 4 = 12.75
```

---

# Key Observation

We only need subarrays of size:

```text
k
```

This is a classic:

```text
Fixed Size Sliding Window
```

problem.

---

# Brute Force Approach

Generate every subarray of size `k`.

Calculate its sum.

Track the maximum.

---

## Python Solution

```python
class Solution:
    def findMaxAverage(self, nums, k):

        max_avg = float('-inf')

        for i in range(len(nums) - k + 1):

            current_sum = 0

            for j in range(i, i + k):
                current_sum += nums[j]

            max_avg = max(max_avg,
                          current_sum / k)

        return max_avg
```

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n × k) |
| Space | O(1) |

### Why O(n × k)?

For every starting position:

```text
n windows
```

we calculate:

```text
k elements
```

---

# Optimal Approach (Sliding Window)

Instead of recalculating the entire sum:

Keep the current window sum.

When moving the window:

```text
Add new element
Remove old element
```

---

# Sliding Window Idea

Window:

```text
[1, 12, -5, -6]
```

Sum:

```text
2
```

Move right:

```text
[12, -5, -6, 50]
```

Instead of recomputing:

```text
Add 50
Remove 1
```

New sum:

```text
2 + 50 - 1 = 51
```

Much faster.

---

## Python Solution

```python
class Solution:
    def findMaxAverage(self, nums, k):

        window_sum = sum(nums[:k])

        max_sum = window_sum

        for i in range(k, len(nums)):

            window_sum += nums[i]
            window_sum -= nums[i - k]

            max_sum = max(max_sum, window_sum)

        return max_sum / k
```

---

# Dry Run

Input:

```python
nums = [1,12,-5,-6,50,3]
k = 4
```

---

### Initial Window

```python
[1,12,-5,-6]
```

Sum:

```python
2
```

```python
max_sum = 2
```

---

### Move Window

Add:

```python
50
```

Remove:

```python
1
```

New sum:

```python
2 + 50 - 1 = 51
```

Update:

```python
max_sum = 51
```

---

### Move Window Again

Add:

```python
3
```

Remove:

```python
12
```

New sum:

```python
51 + 3 - 12 = 42
```

```python
max_sum = 51
```

---

### Final Answer

```python
51 / 4
```

Output:

```python
12.75
```

---

# Visualization

```text
Window Size = 4

[1,12,-5,-6]  Sum = 2

   [12,-5,-6,50]  Sum = 51

      [-5,-6,50,3]  Sum = 42
```

Maximum:

```text
51
```

Average:

```text
12.75
```

---

# Why Does This Work?

Every window overlaps heavily with the previous one.

Example:

```text
[1,12,-5,-6]

[12,-5,-6,50]
```

Only two elements changed:

```text
Remove 1
Add 50
```

So we reuse previous work.

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(1) |

### Why O(n)?

Each element enters and leaves the window exactly once.

---

### Why O(1) Space?

Only a few variables are used:

```python
window_sum
max_sum
```

---

# Java Solution

```java
class Solution {

    public double findMaxAverage(int[] nums, int k) {

        int windowSum = 0;

        for(int i = 0; i < k; i++) {
            windowSum += nums[i];
        }

        int maxSum = windowSum;

        for(int i = k; i < nums.length; i++) {

            windowSum += nums[i];
            windowSum -= nums[i - k];

            maxSum = Math.max(maxSum, windowSum);
        }

        return (double) maxSum / k;
    }
}
```

---

# Interview Insight

This is usually the first Sliding Window problem people learn.

It introduces:

```text
Fixed Size Sliding Window
```

The key trick:

```text
Add New Element
Remove Old Element
```

instead of recomputing the entire window.

---

# Pattern Recognition

Whenever you hear:

- Subarray of size K
- Window size K
- Fixed length K
- Maximum sum of size K
- Average of size K

Think:

```text
Fixed Sliding Window
```

---

# Key Takeaways

✅ Window size never changes

✅ Reuse previous window sum

✅ Add incoming element

✅ Remove outgoing element

✅ O(n) instead of O(n × k)

✅ Classic Fixed Sliding Window problem

---

# Related Problems

1. Maximum Sum Subarray of Size K
2. Sliding Window Maximum
3. Find K Closest Elements
4. Diet Plan Performance
5. Number of Subarrays of Size K

These all use the Fixed Sliding Window pattern.

---

# Golden Rule Learned

```text
Exactly K Elements
        ↓
Fixed Sliding Window
```

This is the foundation for almost every Sliding Window problem you'll encounter in interviews.
