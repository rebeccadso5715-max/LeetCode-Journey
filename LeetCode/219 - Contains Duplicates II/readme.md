# LeetCode #219 — Contains Duplicate II

**Difficulty:** Easy

---

# Problem

Given an integer array `nums` and an integer `k`.

Return:

```python
True
```

if there exist two distinct indices:

```text
i and j
```

such that:

```text
nums[i] == nums[j]
```

and

```text
|i - j| <= k
```

Otherwise return:

```python
False
```

---

## Example

### Input

```python
nums = [1, 2, 3, 1]
k = 3
```

### Output

```python
True
```

### Explanation

```text
Index 0 → 1
Index 3 → 1
```

Distance:

```text
3 - 0 = 3
```

Since:

```text
3 <= k
```

Answer:

```python
True
```

---

# Key Observation

We are not checking duplicates in the entire array.

We only care about duplicates within:

```text
Distance ≤ k
```

This immediately suggests:

```text
Sliding Window
```

because we only need to remember the last `k` elements.

---

# Brute Force Approach

For every element:

Check the next `k` positions.

---

## Python Solution

```python
class Solution:
    def containsNearbyDuplicate(self, nums, k):

        n = len(nums)

        for i in range(n):

            for j in range(i + 1,
                           min(i + k + 1, n)):

                if nums[i] == nums[j]:
                    return True

        return False
```

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n × k) |
| Space | O(1) |

---

# Optimal Approach (Sliding Window + Hash Set)

Maintain a window containing:

```text
At most k elements
```

inside a Hash Set.

---

## Idea

When processing:

```python
nums[right]
```

the set should contain only elements whose indices differ by at most:

```text
k
```

If:

```python
nums[right] in window
```

then a nearby duplicate exists.

Return:

```python
True
```

---

## Python Solution

```python
class Solution:
    def containsNearbyDuplicate(self, nums, k):

        window = set()
        left = 0

        for right in range(len(nums)):

            if right - left > k:
                window.remove(nums[left])
                left += 1

            if nums[right] in window:
                return True

            window.add(nums[right])

        return False
```

---

# Dry Run

Input:

```python
nums = [1, 2, 3, 1]
k = 3
```

Initial:

```python
window = {}
left = 0
```

---

### right = 0

```python
window = {1}
```

---

### right = 1

```python
window = {1, 2}
```

---

### right = 2

```python
window = {1, 2, 3}
```

---

### right = 3

Current number:

```python
1
```

Check:

```python
1 in window ?
```

Yes ✅

Return:

```python
True
```

---

# Visualization

```text
k = 3

Window

[1]
[1,2]
[1,2,3]

Next Number = 1

Already Exists
        ↓
      True
```

---

# Example Where Window Shrinks

Input:

```python
nums = [1,2,3,4,1]
k = 2
```

---

### Window

```text
[1,2]
```

Move forward:

```text
[2,3]
```

Move forward:

```text
[3,4]
```

Move forward:

```text
[4,1]
```

The first `1` is no longer inside the window.

Therefore:

```python
False
```

---

# Why Does This Work?

At any moment:

```text
Window Size ≤ k
```

The Hash Set contains exactly the values that are allowed to match.

If a duplicate appears:

```text
within k distance
```

it will already exist inside the set.

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(k) |

### Why O(n)?

Each element:

```text
Added once
Removed once
```

Hash Set operations are O(1) average.

---

### Why O(k)?

Window stores at most:

```text
k elements
```

---

# Java Solution

```java
import java.util.HashSet;

class Solution {

    public boolean containsNearbyDuplicate(
        int[] nums,
        int k
    ) {

        HashSet<Integer> window =
            new HashSet<>();

        int left = 0;

        for(int right = 0;
            right < nums.length;
            right++) {

            if(right - left > k) {

                window.remove(nums[left]);
                left++;
            }

            if(window.contains(nums[right])) {
                return true;
            }

            window.add(nums[right]);
        }

        return false;
    }
}
```

---

# Interview Insight

This problem combines:

```text
Sliding Window
+
Hash Set
```

The window controls:

```text
Distance Constraint
```

The Hash Set provides:

```text
O(1) Duplicate Checking
```

---

# Pattern Recognition

Whenever you hear:

- Nearby Duplicate
- Within K Distance
- Last K Elements
- Recent Elements
- Sliding Range

Think:

```text
Sliding Window
+
Hash Set
```

---

# Sliding Window Pattern Categories

## 1. Fixed Size Window

Example:

```text
Maximum Average Subarray I
```

Window size never changes.

---

## 2. Variable Size Window

Examples:

```text
Longest Substring
Minimum Window
```

Window expands and shrinks dynamically.

---

## 3. Window + Hash Set

Examples:

```text
Contains Duplicate II
Longest Substring Without Repeating Characters
```

Used when:

```text
Need fast membership checking
```

---

## 4. Window + Hash Map

Examples:

```text
Minimum Window Substring
Permutation in String
```

Used when:

```text
Need frequency counting
```

---

# Key Takeaways

✅ Only care about duplicates within distance `k`

✅ Maintain a sliding window of size at most `k`

✅ Use a Hash Set for O(1) lookup

✅ Remove elements that leave the window

✅ O(n) time

✅ O(k) space

✅ Classic Sliding Window + Hash Set problem

---

# Related Problems

1. Contains Duplicate (#217)
2. Longest Substring Without Repeating Characters (#3)
3. Permutation in String (#567)
4. Minimum Window Substring (#76)
5. Find All Anagrams in a String (#438)

These all combine Sliding Window with Hashing.

---

# Golden Rule Learned

```text
Need to check duplicates
within a moving range?
          ↓
Sliding Window
      +
 Hash Set
```

This is one of the most common hybrid interview patterns.
