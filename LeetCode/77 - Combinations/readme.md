# LeetCode #77 — Combinations

**Difficulty:** Medium

---

# Problem

Given two integers:

```python
n
k
```

Return:

```text
All Possible Combinations
```

of:

```text
k numbers
```

chosen from:

```text
1 to n
```

---

## Example

### Input

```python
n = 4
k = 2
```

### Output

```python
[
 [1,2],
 [1,3],
 [1,4],
 [2,3],
 [2,4],
 [3,4]
]
```

---

# What is a Combination?

Combination means:

```text
Order Does NOT Matter
```

Example:

```text
[1,2]
```

and

```text
[2,1]
```

are considered:

```text
Same Combination
```

---

# Combination vs Permutation

### Combination

```text
[1,2]

[2,1]
```

Counted once.

---

### Permutation

```text
[1,2]

[2,1]
```

Counted separately.

---

# Key Observation

We need:

```text
All Possible Combinations
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

Build combinations one number at a time.

Once we pick:

```text
1
```

we only consider:

```text
2,3,4...
```

This prevents duplicates.

---

# Why Use start?

Suppose:

```python
[1]
```

is already chosen.

Next choices:

```text
2
3
4
```

Not:

```text
1
```

again.

This guarantees:

```text
No Duplicate Combinations
```

---

# Python Solution

```python
class Solution:

    def combine(self, n, k):

        result = []

        path = []

        def backtrack(start):

            if len(path) == k:

                result.append(path[:])

                return

            for i in range(
                start,
                n + 1
            ):

                path.append(i)

                backtrack(i + 1)

                path.pop()

        backtrack(1)

        return result
```

---

# Understanding the Code

## Base Case

```python
if len(path) == k:
```

A valid combination is formed.

Save it.

```python
result.append(path[:])
```

---

## Loop

```python
for i in range(start, n + 1)
```

Try every remaining number.

---

## Choose

```python
path.append(i)
```

Take current number.

---

## Explore

```python
backtrack(i + 1)
```

Move forward.

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
n = 4

k = 2
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

Length:

```text
2
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

Choose:

```text
3
```

Save:

```python
[1,3]
```

---

Choose:

```text
4
```

Save:

```python
[1,4]
```

---

Continue.

Final:

```python
[
 [1,2],
 [1,3],
 [1,4],
 [2,3],
 [2,4],
 [3,4]
]
```

---

# Recursion Tree

```text
                    []

          /      |      |      \

        [1]    [2]    [3]    [4]

       / | \     \      \

   [1,2][1,3][1,4]

        [2,3][2,4]

             [3,4]
```

Every leaf of length:

```text
k
```

becomes an answer.

---

# Why Does i + 1 Matter?

Without:

```python
backtrack(i + 1)
```

we could generate:

```text
[1,2]

[2,1]
```

Duplicates.

Using:

```python
i + 1
```

forces increasing order.

---

# Complexity Analysis

Number of combinations:

```text
nCk
```

---

## Time Complexity

```text
O(k × nCk)
```

because:

```text
nCk combinations
```

and copying each answer takes:

```text
O(k)
```

---

## Space Complexity

```text
O(k)
```

Maximum recursion depth:

```text
k
```

---

# Java Solution

```java
class Solution {

    List<List<Integer>> result =
        new ArrayList<>();

    List<Integer> path =
        new ArrayList<>();

    public List<List<Integer>>
        combine(int n, int k) {

        backtrack(
            1,
            n,
            k
        );

        return result;
    }

    private void backtrack(
        int start,
        int n,
        int k
    ) {

        if(path.size() == k) {

            result.add(
                new ArrayList<>(path)
            );

            return;
        }

        for(int i = start;
            i <= n;
            i++) {

            path.add(i);

            backtrack(
                i + 1,
                n,
                k
            );

            path.remove(
                path.size() - 1
            );
        }
    }
}
```

---

# Interview Insight

This introduces the:

```text
Start Index Pattern
```

which is heavily used in:

- Combination Sum
- Subsets II
- Combination Sum II
- Letter Combinations

---

# Core Backtracking Patterns

## 1. Subsets

```text
Take
or
Skip
```

Example:

```text
#78
Subsets
```

---

## 2. Permutations

```text
Choose Unused Element
```

Example:

```text
#46
Permutations
```

---

## 3. Combinations

```text
Choose Next Element
Using Start Index
```

Example:

```text
#77
Combinations
```

---

## 4. Decision Trees

Every choice creates:

```text
New Branch
```

---

## 5. Generate All Possibilities

Backtracking systematically explores:

```text
Every Valid Path
```

---

# How To Identify Backtracking

Look for:

- Generate All
- Return All
- Possible Combinations
- Possible Permutations
- All Subsets
- All Paths
- All Arrangements

Immediate clue:

```text
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

Using:

```python
backtrack(start + 1)
```

instead of:

```python
backtrack(i + 1)
```

Incorrect traversal.

---

## Mistake 3

Appending:

```python
path
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
path.append(i)

backtrack(i + 1)

path.pop()
```

---

# Key Takeaways

✅ Combinations ignore order

✅ Uses Backtracking

✅ Uses Start Index Pattern

✅ Prevents duplicates naturally

✅ Generates all valid combinations

✅ Foundation for advanced backtracking

---

# Related Problems

1. Subsets (#78)
2. Permutations (#46)
3. Combination Sum (#39)
4. Combination Sum II (#40)
5. Letter Combinations (#17)

All use Backtracking.

---

# Golden Rule Learned

```text
Need All Combinations?
         ↓
Use Start Index
         ↓
Backtracking
```

Combinations teach the **Start Index Backtracking Pattern**, one of the most useful techniques for avoiding duplicates while generating all valid possibilities.
