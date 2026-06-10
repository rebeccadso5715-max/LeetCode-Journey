# LeetCode #78 — Subsets

**Difficulty:** Medium

---

# Problem

Given an integer array:

```python
nums
```

Return:

```text
All Possible Subsets
```

The solution set must not contain duplicate subsets.

---

## Example

### Input

```python
nums = [1,2,3]
```

### Output

```python
[
 [],
 [1],
 [2],
 [3],
 [1,2],
 [1,3],
 [2,3],
 [1,2,3]
]
```

---

# Key Observation

For every number:

```text
We have two choices.
```

### Choice 1

Take it.

### Choice 2

Don't take it.

---

Example:

```python
[1,2]
```

For:

```text
1
```

Choose:

```text
Take 1
```

or

```text
Skip 1
```

For:

```text
2
```

Again:

```text
Take 2
```

or

```text
Skip 2
```

---

# Why Backtracking?

The problem asks for:

```text
All Possible Subsets
```

Huge clue:

```text
Generate All
```

Think:

```text
Backtracking
```

---

# Backtracking Idea

At every index:

```text
Take Number
```

or

```text
Skip Number
```

This creates a decision tree.

---

# Visualization

Input:

```python
[1,2]
```

Tree:

```text
            []
         /      \
       [1]      []
      /   \    /  \
 [1,2] [1] [2] []
```

Every leaf becomes an answer.

---

# Recursive Thinking

Suppose:

```python
nums = [1,2,3]
```

At index:

```python
i
```

We decide:

```text
Include nums[i]
```

or

```text
Exclude nums[i]
```

Then solve the remaining problem.

---

# Python Solution

```python
class Solution:

    def subsets(self, nums):

        result = []

        subset = []

        def dfs(i):

            if i >= len(nums):

                result.append(
                    subset.copy()
                )

                return

            subset.append(nums[i])

            dfs(i + 1)

            subset.pop()

            dfs(i + 1)

        dfs(0)

        return result
```

---

# Understanding the Code

## Base Case

```python
if i >= len(nums):
```

We processed all elements.

Save current subset.

```python
result.append(
    subset.copy()
)
```

---

## Choose

```python
subset.append(nums[i])
```

Take current number.

---

## Explore

```python
dfs(i + 1)
```

Move to next index.

---

## Unchoose

```python
subset.pop()
```

Undo the choice.

---

## Skip

```python
dfs(i + 1)
```

Explore path without current number.

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

Take:

```text
1
```

Subset:

```text
[1]
```

---

Take:

```text
2
```

Subset:

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

Skip:

```text
2
```

Save:

```python
[1]
```

---

Backtrack:

```text
[]
```

Skip:

```text
1
```

---

Take:

```text
2
```

Save:

```python
[2]
```

---

Skip:

```text
2
```

Save:

```python
[]
```

---

Final Answer

```python
[
 [1,2],
 [1],
 [2],
 []
]
```

---

# Full Recursion Tree

```text
                    []

             Take 1      Skip 1

              /             \

           [1]              []

        /      \         /      \

   [1,2]      [1]     [2]      []
```

Each leaf is a subset.

---

# Why Use copy()?

Wrong:

```python
result.append(subset)
```

All answers point to the same list.

---

Correct:

```python
result.append(
    subset.copy()
)
```

Creates a snapshot.

---

# Complexity Analysis

## Number of Subsets

For every element:

```text
Take
or
Skip
```

Two choices.

For:

```text
n elements
```

Total subsets:

:contentReference[oaicite:0]{index=0}

---

## Time Complexity

```text
O(n × 2^n)
```

Because:

```text
2^n subsets
```

and each subset copy can take:

```text
O(n)
```

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

    List<Integer> subset =
        new ArrayList<>();

    public List<List<Integer>>
        subsets(int[] nums) {

        dfs(0, nums);

        return result;
    }

    private void dfs(
        int i,
        int[] nums
    ) {

        if(i >= nums.length) {

            result.add(
                new ArrayList<>(subset)
            );

            return;
        }

        subset.add(nums[i]);

        dfs(i + 1, nums);

        subset.remove(
            subset.size() - 1
        );

        dfs(i + 1, nums);
    }
}
```

---

# Interview Insight

This is often the first real Backtracking problem.

It teaches:

```text
Choose
Explore
Unchoose
```

which is the foundation of:

- Permutations
- Combination Sum
- N-Queens
- Sudoku Solver

---

# Pattern Recognition

Whenever you hear:

- All Subsets
- Power Set
- Every Combination
- Include or Exclude

Think:

```text
Backtracking
```

---

# Common Mistakes

## Mistake 1

Forgetting:

```python
subset.pop()
```

Backtracking fails.

---

## Mistake 2

Using:

```python
result.append(subset)
```

instead of:

```python
subset.copy()
```

---

## Mistake 3

Missing base case.

Without:

```python
if i >= len(nums)
```

recursion never stops.

---

# Backtracking Cheat Sheet

```python
Choose

Explore

Unchoose
```

Code:

```python
subset.append(nums[i])

dfs(i + 1)

subset.pop()
```

---

# Key Takeaways

✅ Every element has two choices

✅ Take or Skip

✅ Uses Backtracking

✅ Recursion tree has 2ⁿ leaves

✅ Time = O(n × 2ⁿ)

✅ Space = O(n)

✅ Foundation of many hard problems

---

# Related Problems

1. Permutations (#46)
2. Combination Sum (#39)
3. Generate Parentheses (#22)
4. N-Queens (#51)
5. Sudoku Solver (#37)

All use the same backtracking framework.

---

# Golden Rule Learned

```text
For Every Element

Take It
   or
Skip It
```

This simple idea generates all subsets and forms the foundation of Backtracking.
