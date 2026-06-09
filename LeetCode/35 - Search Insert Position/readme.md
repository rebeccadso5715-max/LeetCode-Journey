# LeetCode #35 — Search Insert Position

**Difficulty:** Easy

---

# Problem

Given a sorted array of distinct integers `nums` and a target value `target`.

Return:

- The index if the target exists.
- Otherwise, return the index where it would be inserted to keep the array sorted.

---

## Example 1

### Input

```python
nums = [1,3,5,6]
target = 5
```

### Output

```python
2
```

Explanation:

```python
nums[2] = 5
```

Target already exists.

---

## Example 2

### Input

```python
nums = [1,3,5,6]
target = 2
```

### Output

```python
1
```

Explanation:

```text
1 < 2 < 3
```

So `2` should be inserted at index:

```python
1
```

Result:

```python
[1,2,3,5,6]
```

---

## Example 3

### Input

```python
nums = [1,3,5,6]
target = 7
```

### Output

```python
4
```

Explanation:

```text
7 is larger than every element.
```

Insert at the end.

---

# Key Observation

The array is:

```text
Sorted
```

And we need to find:

```text
Target
OR
Its Correct Position
```

This is a Binary Search problem.

---

# Brute Force Approach

Scan the array.

Find the first element:

```python
>= target
```

Return its index.

If none exists:

```python
return len(nums)
```

---

## Python Solution

```python
class Solution:
    def searchInsert(self, nums, target):

        for i in range(len(nums)):

            if nums[i] >= target:
                return i

        return len(nums)
```

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(1) |

---

# Optimal Approach (Binary Search)

Use normal Binary Search.

If target is found:

```python
return mid
```

Otherwise:

When the loop ends:

```python
left
```

automatically points to the correct insertion position.

---

# Important Insight

At the end of Binary Search:

```python
right < left
```

And:

```python
left
```

is the first index where:

```python
nums[index] >= target
```

That is exactly where the target should be inserted.

---

## Python Solution

```python
class Solution:
    def searchInsert(self, nums, target):

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

        return left
```

---

# Dry Run

Input:

```python
nums = [1,3,5,6]
target = 2
```

---

### Iteration 1

```python
left = 0
right = 3

mid = 1
```

Value:

```python
nums[1] = 3
```

Since:

```python
3 > 2
```

Move:

```python
right = 0
```

---

### Iteration 2

```python
left = 0
right = 0

mid = 0
```

Value:

```python
nums[0] = 1
```

Since:

```python
1 < 2
```

Move:

```python
left = 1
```

---

Now:

```python
left = 1
right = 0
```

Loop ends.

Return:

```python
left
```

Answer:

```python
1
```

---

# Visualization

```text
nums = [1,3,5,6]
target = 2

       mid
        ↓

1  3  5  6

2 < 3

Search Left

---------

mid
 ↓

1  3  5  6

2 > 1

Search Right

---------

left = 1
right = 0

Stop

Return left = 1
```

---

# Why Return `left`?

Consider:

```python
nums = [1,3,5,6]
target = 4
```

Final state:

```python
left = 2
right = 1
```

Insertion position:

```python
index = 2
```

Result:

```python
[1,3,4,5,6]
```

Exactly correct.

---

# Edge Cases

## Insert at Beginning

Input:

```python
nums = [3,5,7]
target = 1
```

Output:

```python
0
```

---

## Insert at End

Input:

```python
nums = [1,3,5]
target = 10
```

Output:

```python
3
```

---

## Target Exists

Input:

```python
nums = [1,3,5,6]
target = 5
```

Output:

```python
2
```

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(log n) |
| Space | O(1) |

### Why O(log n)?

Each iteration eliminates half the search space.

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
class Solution {

    public int searchInsert(
        int[] nums,
        int target
    ) {

        int left = 0;
        int right = nums.length - 1;

        while(left <= right) {

            int mid =
                (left + right) / 2;

            if(nums[mid] == target) {
                return mid;
            }

            else if(nums[mid] < target) {
                left = mid + 1;
            }

            else {
                right = mid - 1;
            }
        }

        return left;
    }
}
```

---

# Interview Insight

This is usually the first Binary Search boundary problem.

The important lesson:

```text
Binary Search is not only for searching.
```

It can also find:

- Insertion positions
- First occurrence
- Last occurrence
- Lower bound
- Upper bound

---

# Pattern Recognition

Whenever you hear:

- Insert Position
- First Position ≥ Target
- Lower Bound
- Sorted Array

Think:

```text
Binary Search
```

---

# Key Takeaways

✅ Array is sorted

✅ Standard Binary Search

✅ Return index if target exists

✅ Return `left` if target doesn't exist

✅ `left` becomes insertion position

✅ O(log n) time

✅ O(1) space

---

# Related Problems

1. Binary Search (#704)
2. Find First and Last Position (#34)
3. First Bad Version (#278)
4. Search in Rotated Sorted Array (#33)
5. Koko Eating Bananas (#875)

These are all Binary Search variations.

---

# Golden Rule Learned

```text
Target Not Found?
        ↓
Return left
```

In many Binary Search boundary problems, `left` ends up pointing exactly where the target belongs.
