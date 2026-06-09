# LeetCode #167 — Two Sum II: Input Array Is Sorted

**Difficulty:** Easy

---

# Problem

Given a **1-indexed sorted array** `numbers` and a target value, find two numbers such that:

```text
numbers[i] + numbers[j] = target
```

Return their indices:

```python
[index1, index2]
```

where:

```text
1 ≤ index1 < index2 ≤ n
```

---

## Example

### Input

```python
numbers = [2, 7, 11, 15]
target = 9
```

### Output

```python
[1, 2]
```

### Explanation

```text
numbers[0] + numbers[1]
=
2 + 7
=
9
```

Since the problem uses 1-based indexing:

```python
[1, 2]
```

---

# Brute Force Approach

Check every possible pair.

```python
for i in range(n):
    for j in range(i + 1, n):

        if numbers[i] + numbers[j] == target:
            return [i + 1, j + 1]
```

---

## Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n²) |
| Space | O(1) |

---

# Key Observation

The array is already sorted.

```python
[2, 7, 11, 15]
```

This allows us to use the **Two Pointer Technique**.

---

# Optimal Approach (Two Pointers)

Maintain:

```python
left = 0
right = len(numbers) - 1
```

At every step:

```python
total = numbers[left] + numbers[right]
```

---

### If total == target

Answer found.

---

### If total < target

Need a larger sum.

Move:

```python
left += 1
```

because moving left rightward increases the value.

---

### If total > target

Need a smaller sum.

Move:

```python
right -= 1
```

because moving right leftward decreases the value.

---

## Python Solution

```python
class Solution:
    def twoSum(self, numbers, target):

        left = 0
        right = len(numbers) - 1

        while left < right:

            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]

            elif total < target:
                left += 1

            else:
                right -= 1
```

---

# Dry Run

Input:

```python
numbers = [2, 7, 11, 15]
target = 9
```

Initial:

```python
left = 0
right = 3
```

---

### Iteration 1

```python
2 + 15 = 17
```

Too large.

Move:

```python
right -= 1
```

Now:

```python
left = 0
right = 2
```

---

### Iteration 2

```python
2 + 11 = 13
```

Still too large.

Move:

```python
right -= 1
```

Now:

```python
left = 0
right = 1
```

---

### Iteration 3

```python
2 + 7 = 9
```

Target found ✅

Return:

```python
[1, 2]
```

---

# Visualization

```text
Target = 9

[2, 7, 11, 15]

 L          R

2 + 15 = 17
Too Large

Move R

[2, 7, 11, 15]

 L      R

2 + 11 = 13
Too Large

Move R

[2, 7, 11, 15]

 L  R

2 + 7 = 9

Answer Found
```

---

# Why Does This Work?

Because the array is sorted.

Suppose:

```python
total < target
```

Current number at `left` is too small.

Moving `right` leftward would make the sum even smaller.

So the only useful move is:

```python
left += 1
```

---

Suppose:

```python
total > target
```

Current number at `right` is too large.

Moving `left` rightward would make the sum even larger.

So the only useful move is:

```python
right -= 1
```

---

Each move eliminates impossible combinations.

This is what makes the algorithm O(n).

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(1) |

### Why O(n)?

Each pointer moves at most:

```text
n times
```

Total work:

```text
O(n)
```

---

### Why O(1) Space?

Only two variables are used:

```python
left
right
```

---

# Java Solution

```java
class Solution {

    public int[] twoSum(int[] numbers, int target) {

        int left = 0;
        int right = numbers.length - 1;

        while(left < right) {

            int total = numbers[left] + numbers[right];

            if(total == target) {
                return new int[]{
                    left + 1,
                    right + 1
                };
            }

            else if(total < target) {
                left++;
            }

            else {
                right--;
            }
        }

        return new int[]{};
    }
}
```

---

# Interview Insight

This problem introduces the most important Two Pointer pattern:

## Opposite Direction Pointers

```text
left  ->      <-  right
```

Used when:

- Array is sorted
- Need pairs
- Need target sum
- Need comparisons from both ends

---

# Three Major Two Pointer Patterns

## 1. Opposite Direction

```text
left  ->      <- right
```

Examples:

- Two Sum II
- Valid Palindrome
- Container With Most Water

---

## 2. Same Direction

```text
slow -> -> fast
```

Examples:

- Remove Duplicates
- Move Zeroes
- Linked List Cycle

---

## 3. Sliding Window

```text
left -> -> right
```

Examples:

- Longest Substring Without Repeating Characters
- Minimum Size Subarray Sum
- Maximum Average Subarray

---

# Key Takeaways

✅ Array is sorted

✅ Sorting enables Two Pointers

✅ Move left when sum is too small

✅ Move right when sum is too large

✅ Each move removes impossible answers

✅ O(n) time and O(1) space

✅ Foundation of many medium and hard problems

---

# Related Problems

1. Valid Palindrome
2. Container With Most Water
3. 3Sum
4. 4Sum
5. Move Zeroes
6. Remove Duplicates from Sorted Array
7. Longest Substring Without Repeating Characters

Master this problem and you'll understand the core idea behind the Two Pointer technique.
