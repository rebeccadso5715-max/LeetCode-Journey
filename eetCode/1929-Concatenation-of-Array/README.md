# LeetCode 1929 - Concatenation of Array

## Difficulty

Easy

---

## Problem

Given an integer array `nums` of length `n`, return an array `ans` of length `2n` where:

```text
ans[i] = nums[i]
ans[i + n] = nums[i]
```

---

## Example

Input:

```text
[1,2,1]
```

Output:

```text
[1,2,1,1,2,1]
```

---

## Brute Force Approach

Copy elements twice into a new array.

### Algorithm

1. Create empty answer array.
2. Traverse nums and append elements.
3. Traverse nums again and append elements.
4. Return answer.

### Complexity

Time: O(n)

Space: O(n)

---

## Optimal Approach

Use direct concatenation.

### Complexity

Time: O(n)

Space: O(n)

---

## Interview Insight

Since the output size is 2n, any solution must at least write 2n elements.

Therefore, a runtime better than O(n) is impossible.
