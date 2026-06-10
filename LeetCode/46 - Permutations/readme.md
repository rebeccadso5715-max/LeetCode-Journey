# LeetCode #46 — Permutations

**Difficulty:** Medium

---

# Problem

Given an array of distinct integers:

```python
nums
```

Return:

```text
All Possible Permutations
```

A permutation is:

```text
A rearrangement of elements.
```

---

## Example

### Input

```python
nums = [1,2,3]
```

### Output

```python
[
 [1,2,3],
 [1,3,2],
 [2,1,3],
 [2,3,1],
 [3,1,2],
 [3,2,1]
]
```

---

# What is a Permutation?

For:

```python
[1,2]
```

Possible arrangements:

```text
[1,2]

[2,1]
```

---

For:

```python
[1,2,3]
```

Possible arrangements:

```text
123

132

213

231

312

321
```

Total:

```text
6
```

---

# Key Observation

At every position:

```text
Choose one unused number.
```

Then:

```text
Recursively fill
remaining positions.
```

Huge clue:

```text
Generate All Arrangements
```

Think:

```text
Backtracking
```

---

# Backtracking Idea

For each position:

```text
Try every unused number.
```

After exploring:

```text
Undo the choice.
```

Then try another number.

---

# Visualization

Input:

```python
[1,2,3]
```

Start:

```text
[]
```

Choose:

```text
1
```

Path:

```text
[1]
```

Choose:

```text
2
```

Path:

```text
[1,2]
```

Choose:

```text
3
```

Path:

```text
[1,2,3]
```

Save answer.

Backtrack.

Try:

```text
[1,3,2]
```

Continue.

---

# Recursion Tree

```text
                    []

           /          |          \

         [1]         [2]        [3]

        /   \       /   \      /   \

    [1,2] [1,3] [2,1] [2,3] [3,1] [3,2]

      |      |     |      |     |      |

 [1,2,3] [1,3,2] ...
```

Every leaf is a permutation.

---

# Python Solution

```python
class Solution:

    def permute(self, nums):

        result = []

        def backtrack(path):

            if len(path) == len(nums):

                result.append(path[:])

                return

            for num in nums:

                if num in path:
                    continue

                path.append(num)

                backtrack(path)

                path.pop()

        backtrack([])

        return result
```

---

# Understanding the Code

## Base Case

```python
if len(path) == len(nums):
```

A complete permutation is formed.

Save it.

```python
result.append(path[:])
```

---

## Try Every Number

```python
for num in nums:
```

Attempt to place every number.

---

## Skip Used Numbers

```python
if num in path:
    continue
```

A permutation cannot reuse elements.

---

## Choose

```python
path.append(num)
```

Add current number.

---

## Explore

```python
backtrack(path)
```

Build the remaining permutation.

---

## Unchoose

```python
path.pop()
```

Backtrack.

---

# Dry Run

Input:

```python
[1,2]
```

---

Start:

```text
[]
```

---

Choose:

```text
1
```

Path:

```text
[1]
```

---

Choose:

```text
2
```

Path:

```text
[1,2]
```

Save:

```python
[1,2]
```

---

Backtrack:

```text
[1]
```

---

Backtrack:

```text
[]
```

---

Choose:

```text
2
```

Path:

```text
[2]
```

---

Choose:

```text
1
```

Path:

```text
[2,1]
```

Save:

```python
[2,1]
```

---

Answer:

```python
[
 [1,2],
 [2,1]
]
```

---

# Why Use path[:]?

Wrong:

```python
result.append(path)
```

All answers reference the same list.

---

Correct:

```python
result.append(path[:])
```

Creates a copy.

---

# Complexity Analysis

## Number of Permutations

For:

```text
n numbers
```

Choices:

```text
n

n-1

n-2

...
```

Total:

```text
n!
```

---

## Time Complexity

:contentReference[oaicite:0]{index=0}

We generate every permutation.

---

## Space Complexity

```text
O(n)
```

Recursion depth:

```text
n
```

---

# Java Solution

```java
class Solution {

    List<List<Integer>> result =
        new ArrayList<>();

    public List<List<Integer>>
        permute(int[] nums) {

        backtrack(
            new ArrayList<>(),
            nums
        );

        return result;
    }

    private void backtrack(
        List<Integer> path,
        int[] nums
    ) {

        if(path.size() ==
           nums.length) {

            result.add(
                new ArrayList<>(path)
            );

            return;
        }

        for(int num : nums) {

            if(path.contains(num))
                continue;

            path.add(num);

            backtrack(path, nums);

            path.remove(
                path.size() - 1
            );
        }
    }
}
```

---

# Interview Insight

Subsets used:

```text
Take / Skip
```

Permutations use:

```text
Choose One Unused Element
```

This is a different backtracking pattern.

---

# Subsets vs Permutations

| Problem | Choice |
|----------|---------|
| Subsets | Take / Skip |
| Permutations | Pick Unused Number |

---

# Pattern Recognition

Whenever you hear:

- All Arrangements
- All Orderings
- Rearrange Elements
- Every Possible Ordering

Think:

```text
Permutations
+
Backtracking
```

---

# Common Mistakes

## Mistake 1

Forgetting:

```python
path.pop()
```

No backtracking occurs.

---

## Mistake 2

Not skipping used elements.

```python
if num in path:
```

is necessary.

---

## Mistake 3

Using:

```python
result.append(path)
```

instead of:

```python
path[:]
```

---

# Backtracking Cheat Sheet

```python
Choose

Explore

Unchoose
```

Code:

```python
path.append(num)

backtrack(path)

path.pop()
```

---

# Key Takeaways

✅ Generates all arrangements

✅ Uses Backtracking

✅ Choose unused numbers

✅ Undo choices using pop()

✅ Total permutations = n!

✅ Time = O(n!)

✅ Space = O(n)

---

# Related Problems

1. Subsets (#78)
2. Combination Sum (#39)
3. Generate Parentheses (#22)
4. N-Queens (#51)
5. Sudoku Solver (#37)

All use Backtracking.

---

# Golden Rule Learned

```text
Need All Arrangements?
        ↓
Choose Unused Element
        ↓
Backtracking
```

Permutations is one of the most important backtracking problems and teaches how to systematically generate every possible ordering.
