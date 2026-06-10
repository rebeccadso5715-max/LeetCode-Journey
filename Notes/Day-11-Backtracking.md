# Class 11 — Backtracking

## Why Backtracking Matters

Backtracking is one of the most important interview topics.

It teaches you how to:

- Generate All Possibilities
- Explore Choices
- Undo Decisions
- Search Systematically

Many famous interview problems use backtracking:

- Subsets
- Permutations
- Combination Sum
- N-Queens
- Sudoku Solver
- Generate Parentheses
- Word Search

---

# The Backtracking Mindset

Think:

```text
Try
 ↓
Explore
 ↓
Undo
 ↓
Try Again
```

You make a choice.

If it doesn't work:

```text
Go Back
```

and try another choice.

---

# What is Backtracking?

Imagine a maze.

At every step:

```text
Choose a path
```

If wrong:

```text
Go Back
```

Try another path.

That's Backtracking.

---

# Maze Example

```text
Start

   A
  / \
 B   C
 |
 D

Goal
```

Try:

```text
A → B → D
```

If not correct:

```text
Backtrack
```

Return to:

```text
A
```

Try:

```text
A → C
```

---

# Core Idea

Backtracking explores:

```text
All Possible Choices
```

But only keeps valid answers.

---

# General Template

```python
def backtrack():

    if base_case:

        save_answer

        return

    for choice in choices:

        make_choice

        backtrack()

        undo_choice
```

This template appears in almost every backtracking problem.

---

# The Three Steps

## 1. Choose

Pick an option.

Example:

```python
path.append(num)
```

---

## 2. Explore

Continue recursively.

```python
backtrack()
```

---

## 3. Unchoose

Undo the choice.

```python
path.pop()
```

This is the most important step.

---

# Visualization

Suppose:

```python
nums = [1, 2]
```

Generate all subsets.

---

Start:

```text
[]
```

Choose:

```text
[1]
```

Choose:

```text
[1,2]
```

Save answer.

Backtrack:

```text
[1]
```

Backtrack:

```text
[]
```

Choose:

```text
[2]
```

Save answer.

---

# Why Undo?

Without:

```python
path.pop()
```

choices from previous branches leak into new branches.

Backtracking would fail.

---

# Example 1 — Print All Binary Strings

Length:

```python
n = 2
```

Output:

```text
00

01

10

11
```

---

## Python

```python
def backtrack(path):

    if len(path) == 2:

        print(path)

        return

    for choice in ["0", "1"]:

        path.append(choice)

        backtrack(path)

        path.pop()
```

---

# Recursion Tree

```text
            []

          /    \

        [0]    [1]

       /  \    /  \

   [00] [01] [10] [11]
```

Every path becomes an answer.

---

# Example 2 — Generate Subsets

Input:

```python
[1,2]
```

Output:

```python
[]

[1]

[2]

[1,2]
```

---

## Python

```python
def backtrack(i):

    if i == len(nums):

        result.append(path[:])

        return

    path.append(nums[i])

    backtrack(i + 1)

    path.pop()

    backtrack(i + 1)
```

---

# Recursion Tree

```text
              []

            /     \

         [1]       []

        /   \      /  \

    [1,2] [1]   [2]  []
```

---

# Backtracking vs Recursion

Recursion:

```text
Function Calls Itself
```

Backtracking:

```text
Recursion
+
Undo Choices
```

All backtracking uses recursion.

Not all recursion is backtracking.

---

# Common Interview Clues

Whenever you hear:

```text
Generate All

Find All

Return Every

All Combinations

All Permutations

Every Possible Way
```

Think:

```text
Backtracking
```

---

# Common Mistakes

## Mistake 1

Forgetting to undo.

Wrong:

```python
path.append(x)

backtrack()
```

Correct:

```python
path.append(x)

backtrack()

path.pop()
```

---

## Mistake 2

Appending path directly.

Wrong:

```python
result.append(path)
```

All answers become identical.

Correct:

```python
result.append(path[:])
```

---

## Mistake 3

Missing base case.

Without a stopping condition:

```text
Infinite recursion
```

---

# Complexity

Backtracking often explores:

```text
All Possibilities
```

Typical complexities:

```text
O(2^n)

O(n!)

O(k^n)
```

depending on the problem.

---

# Pattern Recognition

Whenever you hear:

- Subsets
- Permutations
- Combinations
- N-Queens
- Sudoku
- Generate Parentheses
- Word Search

Think:

```text
Backtracking
```

---

# Problems We'll Solve

### Easy

1. Subsets (#78)

### Medium

2. Combination Sum (#39)
3. Permutations (#46)
4. Generate Parentheses (#22)

### Hard

5. N-Queens (#51)
6. Sudoku Solver (#37)

---

# Backtracking Cheat Sheet

```python
make_choice

backtrack()

undo_choice
```

Always remember:

```text
Choose

Explore

Unchoose
```

---

# Key Takeaways

✅ Backtracking explores all possibilities

✅ Uses recursion

✅ Every choice must be undone

✅ Perfect for search problems

✅ Common in interviews

✅ Foundation of many hard problems

---

# Golden Rule Learned

```text
Choose
  ↓
Explore
  ↓
Undo
  ↓
Try Next Choice
```

Backtracking is essentially recursion with the ability to "go back" and try a different path when needed.
