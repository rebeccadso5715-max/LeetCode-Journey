# LeetCode #724 — Find Pivot Index

**Difficulty:** Easy

---

# Problem

Given an integer array `nums`, return the **pivot index**.

The pivot index is the index where:

```text
Sum of all elements to the left
=
Sum of all elements to the right
```

If no such index exists, return `-1`.

---

## Example

### Input

```python
[1, 7, 3, 6, 5, 6]
```

### Output

```python
3
```

### Explanation

Pivot Index = 3

```text
Array: [1, 7, 3, 6, 5, 6]
               ↑

Left Sum  = 1 + 7 + 3 = 11
Right Sum = 5 + 6 = 11
```

Since both sums are equal, return:

```python
3
```

---

# Brute Force Approach

For every index:

1. Calculate the sum of elements on the left.
2. Calculate the sum of elements on the right.
3. Compare them.

If they are equal, return the current index.

---

## Python Solution

```python
class Solution:
    def pivotIndex(self, nums):

        for i in range(len(nums)):

            left = sum(nums[:i])

            right = sum(nums[i + 1:])

            if left == right:
                return i

        return -1
```

---

# Dry Run

Input:

```python
[1, 7, 3, 6, 5, 6]
```

### i = 0

```python
left = 0
right = 27

Not Equal
```

### i = 1

```python
left = 1
right = 20

Not Equal
```

### i = 2

```python
left = 8
right = 17

Not Equal
```

### i = 3

```python
left = 11
right = 11

Equal ✅
```

Return:

```python
3
```

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n²) |
| Space | O(1) |

### Why O(n²)?

For every index, we calculate two sums.

Each `sum()` operation takes O(n).

```text
n × O(n)
=
O(n²)
```

---

# Optimal Approach

Instead of repeatedly calculating sums:

- Compute the total sum once.
- Maintain a running left sum.
- Derive the right sum mathematically.

---

## Key Observation

At any index:

```text
Right Sum
=
Total Sum
-
Left Sum
-
Current Element
```

Formula:

```text
right_sum = total - left_sum - nums[i]
```

If:

```text
left_sum == right_sum
```

Then we found the pivot index.

---

## Python Solution

```python
class Solution:
    def pivotIndex(self, nums):

        total = sum(nums)

        left_sum = 0

        for i in range(len(nums)):

            right_sum = total - left_sum - nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1
```

---

# Dry Run

Input:

```python
nums = [1, 7, 3, 6, 5, 6]
```

### Step 1

```python
total = 28
left_sum = 0
```

---

### i = 0

```python
right_sum = 28 - 0 - 1
          = 27

0 != 27
```

Update:

```python
left_sum = 1
```

---

### i = 1

```python
right_sum = 28 - 1 - 7
          = 20

1 != 20
```

Update:

```python
left_sum = 8
```

---

### i = 2

```python
right_sum = 28 - 8 - 3
          = 17

8 != 17
```

Update:

```python
left_sum = 11
```

---

### i = 3

```python
right_sum = 28 - 11 - 6
          = 11

11 == 11 ✅
```

Return:

```python
3
```

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(1) |

### Why O(n)?

- One pass through the array.
- No repeated sum calculations.

### Why O(1) Space?

Only a few variables are used.

---

# Java Solution

```java
class Solution {

    public int pivotIndex(int[] nums) {

        int total = 0;

        for(int num : nums) {
            total += num;
        }

        int leftSum = 0;

        for(int i = 0; i < nums.length; i++) {

            int rightSum = total - leftSum - nums[i];

            if(leftSum == rightSum) {
                return i;
            }

            leftSum += nums[i];
        }

        return -1;
    }
}
```

---

# Interview Insight

This problem introduces one of the most important interview concepts:

## Prefix Sum

Instead of recalculating sums repeatedly:

```text
Store information from previous elements
and reuse it.
```

---

## Pattern Recognition

Whenever you hear:

- Left Sum
- Right Sum
- Balance Point
- Equal Partition
- Sum Till Index
- Range Sum

Think:

```text
Prefix Sum
```

---

# Key Takeaways

✅ Brute Force repeatedly calculates sums → O(n²)

✅ Prefix Sum avoids recomputation → O(n)

✅ Running left sum is often enough

✅ Right sum can often be derived mathematically

✅ One of the most common interview patterns

---

# Related Problems

- Running Sum of 1D Array (#1480)
- Range Sum Query
- Subarray Sum Equals K
- Continuous Subarray Sum
- Product of Array Except Self
- Maximum Size Subarray Sum Equals K

All of these build upon the Prefix Sum pattern.
