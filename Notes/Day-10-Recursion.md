# Class 10 — Recursion

## Why Recursion Matters

Recursion is one of the most important concepts in Data Structures and Algorithms.

Many advanced topics are built on recursion:

- Trees
- Graphs
- DFS
- Backtracking
- Dynamic Programming
- Divide & Conquer

---

# What is Recursion?

Recursion is when a function calls itself.

Instead of solving the entire problem directly:

```text
Solve a smaller version
of the same problem.
```

---

# Real Life Analogy

Imagine standing between two mirrors.

```text
Mirror
  ↓
Mirror
  ↓
Mirror
  ↓
Mirror
```

The same image repeats again and again.

Recursion works similarly.

A function keeps calling itself until it reaches a stopping condition.

---

# The Two Golden Rules

Every recursive solution needs:

## 1. Base Case

A condition that stops recursion.

Without a base case:

```text
Infinite Recursion
```

Example:

```python
if n == 0:
    return
```

---

## 2. Recursive Call

The function must call itself with a smaller problem.

Example:

```python
countdown(n - 1)
```

The problem size gets smaller each time.

---

# Example 1 — Countdown

Print numbers from:

```text
5 to 1
```

---

## Python Solution

```python
def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)
```

---

# Dry Run

Call:

```python
countdown(3)
```

---

### Step 1

```python
countdown(3)
```

Print:

```text
3
```

Call:

```python
countdown(2)
```

---

### Step 2

```python
countdown(2)
```

Print:

```text
2
```

Call:

```python
countdown(1)
```

---

### Step 3

```python
countdown(1)
```

Print:

```text
1
```

Call:

```python
countdown(0)
```

---

### Step 4

```python
countdown(0)
```

Base case reached.

Stop.

---

# Visualization

```text
countdown(3)

3
↓
countdown(2)

2
↓
countdown(1)

1
↓
countdown(0)

STOP
```

---

# What is the Call Stack?

Every function call is stored inside a stack.

Example:

```python
countdown(3)
```

Stack:

```text
Top
 ↓

countdown(3)
```

---

Calls:

```python
countdown(2)
```

Stack:

```text
countdown(2)

countdown(3)
```

---

Calls:

```python
countdown(1)
```

Stack:

```text
countdown(1)

countdown(2)

countdown(3)
```

---

Calls:

```python
countdown(0)
```

Stack:

```text
countdown(0)

countdown(1)

countdown(2)

countdown(3)
```

---

Base case reached.

Functions start returning.

---

# Example 2 — Factorial

Definition:

```text
5! = 5 × 4 × 3 × 2 × 1
```

---

Observation:

```text
5!
=
5 × 4!
```

Similarly:

```text
4!
=
4 × 3!
```

This is recursion.

---

## Mathematical Formula

:contentReference[oaicite:0]{index=0}

Base case:

```text
0! = 1
```

---

## Python Solution

```python
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)
```

---

# Dry Run

```python
factorial(3)
```

---

```python
3 * factorial(2)
```

↓

```python
3 * (2 * factorial(1))
```

↓

```python
3 * (2 * (1 * factorial(0)))
```

↓

```python
3 * (2 * (1 * 1))
```

↓

```python
6
```

---

# Call Stack Visualization

```text
factorial(3)

factorial(2)

factorial(1)

factorial(0)

Base Case
```

Then:

```text
Return 1

Return 1

Return 2

Return 6
```

---

# Why Recursion Uses Extra Memory

Every function call is stored in memory.

Example:

```python
factorial(1000)
```

creates:

```text
1000 function calls
```

inside the call stack.

Therefore:

```text
Space = O(n)
```

---

# Recursive Thinking Pattern

Ask:

```text
Can I solve this problem
using a smaller version
of itself?
```

If yes:

```text
Recursion might work.
```

---

# Common Mistakes

## Mistake 1

No Base Case

Wrong:

```python
def func(n):

    func(n - 1)
```

Infinite recursion.

---

## Mistake 2

Problem Doesn't Get Smaller

Wrong:

```python
func(n)
```

Same input again.

Infinite recursion.

---

## Mistake 3

Forgetting Return

Wrong:

```python
return n * factorial(n - 1)
```

vs

```python
factorial(n - 1)
```

---

# Recursion vs Iteration

## Iterative

```python
for i in range(n):
```

Uses loops.

---

## Recursive

```python
func(n - 1)
```

Uses function calls.

---

# Complexity Summary

| Factor | Recursion |
|----------|------------|
| Time | Depends on problem |
| Space | Usually O(depth) |
| Uses Call Stack | Yes |
| Needs Base Case | Yes |

---

# When Should You Think Recursion?

Big interview clues:

```text
Tree

Graph DFS

Backtracking

Factorial

Fibonacci

Subsets

Permutations

Divide & Conquer
```

Whenever you see these:

```text
Think Recursion
```

---

# Problems We'll Solve Next

### Easy

1. Fibonacci Number (#509)

### Medium

2. Pow(x,n) (#50)
3. Generate Parentheses (#22)

### Advanced

4. Subsets (#78)
5. Permutations (#46)
6. Combination Sum (#39)

---

# Key Takeaways

✅ Recursion = Function calling itself

✅ Every recursive solution needs:
- Base Case
- Recursive Call

✅ Problem size must decrease

✅ Uses Call Stack

✅ Often simpler than loops

✅ Foundation of Trees, DFS, and Backtracking

---

# Golden Rule Learned

```text
Can Problem Be Solved
Using Smaller Version
Of Itself?
        ↓
     Recursion
```

Recursion is one of the most powerful problem-solving techniques in computer science and appears everywhere in advanced algorithms.
