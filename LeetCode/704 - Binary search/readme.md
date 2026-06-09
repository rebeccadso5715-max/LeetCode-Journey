# LeetCode #704 — Binary Search

**Difficulty:** Easy

---

# Problem

Given a sorted array of integers `nums` and an integer `target`.

Return:

```python
index of target
```

if it exists.

Otherwise return:

```python
-1
```

---

## Example

### Input

```python
nums = [-1,0,3,5,9,12]
target = 9
```

### Output

```python
4
```

### Explanation

```python
nums[4] = 9
```

Therefore:

```python
return 4
```

---

# Key Observation

The array is:

```text
Sorted
```

This is the biggest Binary Search clue.

Instead of checking every element:

```text
O(n)
```

we can repeatedly eliminate half of the search space.

---

# Brute Force Approach

Check every element.

---

## Python Solution

```python
class Solution:
    def search(self, nums, target):

        for i in range(len(nums)):

            if nums[i] == target:
                return i

        return -1
```

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(1) |

---

# Optimal Approach (Binary Search)

Use two pointers:

```python
left = 0
right = len(nums) - 1
```

Search only inside:

```text
[left ... right]
```

---

# Binary Search Template

```python
while left <= right:

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid

    elif nums[mid] < target:
        left = mid + 1

    else:
        right = mid - 1
```

---

# Why Does This Work?

Because the array is sorted.

If:

```python
nums[mid] < target
```

then:

```text
Everything left of mid
is also too small.
```

Discard it.

---

If:

```python
nums[mid] > target
```

then:

```text
Everything right of mid
is also too large.
```

Discard it.

---

# Python Solution

```python
class Solution:
    def search(self, nums, target):

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

        return -1
```

---

# Dry Run

Input:

```python
nums = [-1,0,3,5,9,12]
target = 9
```

---

### Iteration 1

```python
left = 0
right = 5

mid = 2
```

Value:

```python
nums[2] = 3
```

Since:

```python
3 < 9
```

Discard left half.

Move:

```python
left = mid + 1
```

```python
left = 3
```

---

### Iteration 2

```python
left = 3
right = 5

mid = 4
```

Value:

```python
nums[4] = 9
```

Found.

Return:

```python
4
```

---

# Visualization

```text
Initial

-1  0  3  5  9  12
       ↑
      mid

3 < 9

Discard Left Half

----------------

5  9  12
   ↑
  mid

Found
```

---

# Example Where Target Doesn't Exist

Input:

```python
nums = [-1,0,3,5,9,12]
target = 2
```

---

### Step 1

```python
mid = 2
value = 3
```

```python
3 > 2
```

Move:

```python
right = 1
```

---

### Step 2

```python
mid = 0
value = -1
```

```python
-1 < 2
```

Move:

```python
left = 1
```

---

### Step 3

```python
mid = 1
value = 0
```

```python
0 < 2
```

Move:

```python
left = 2
```

Now:

```python
left > right
```

Stop.

Return:

```python
-1
```

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(log n) |
| Space | O(1) |

### Why O(log n)?

Each iteration removes:

```text
Half the remaining elements
```

Example:

```text
64
↓
32
↓
16
↓
8
↓
4
↓
2
↓
1
```

Only:

```text
log₂(n)
```

steps.

---

### Why O(1) Space?

Only a few variables:

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

    public int search(int[] nums, int target) {

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

        return -1;
    }
}
```

---

# Interview Insight

This is the purest Binary Search problem.

Everything else builds on this template.

You should memorize this pattern completely.

---

# Pattern Recognition

Whenever you hear:

- Sorted Array
- Search Target
- Find Element
- Lookup

Think:

```text
Binary Search
```

---

# Common Mistakes

## Mistake 1

Using:

```python
while left < right
```

instead of:

```python
while left <= right
```

---

## Mistake 2

Forgetting:

```python
mid + 1
```

or

```python
mid - 1
```

which can cause infinite loops.

---

## Mistake 3

Applying Binary Search on an unsorted array.

---

# Key Takeaways

✅ Array must be sorted

✅ Find middle element

✅ Eliminate half the search space

✅ O(log n) time

✅ O(1) space

✅ Foundation of all Binary Search problems

---

# Related Problems

1. Search Insert Position (#35)
2. First Bad Version (#278)
3. Find First and Last Position (#34)
4. Search in Rotated Sorted Array (#33)
5. Find Minimum in Rotated Sorted Array (#153)

These are all variations of the same Binary Search template.

---

# Golden Rule Learned

```text
Sorted Array
      +
Search Target
      ↓
Binary Search
```

This is the most important Binary Search pattern and the foundation for every advanced Binary Search problem.
