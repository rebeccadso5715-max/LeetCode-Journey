# LeetCode #509 — Fibonacci Number

**Difficulty:** Easy

---

# Problem

The Fibonacci sequence is defined as:

```text
F(0) = 0

F(1) = 1

F(n) = F(n-1) + F(n-2)
```

for:

```text
n > 1
```

Return:

```python
F(n)
```

---

## Example

### Input

```python
n = 4
```

### Output

```python
3
```

### Explanation

Sequence:

```text
0 1 1 2 3
```

Therefore:

```text
F(4) = 3
```

---

# Key Observation

Each Fibonacci number depends on:

```text
Previous Two Numbers
```

Example:

```text
F(5)

=
F(4) + F(3)
```

This naturally suggests:

```text
Recursion
```

---

# Recursive Solution

## Python

```python
class Solution:
    def fib(self, n):

        if n <= 1:
            return n

        return (
            self.fib(n - 1)
            +
            self.fib(n - 2)
        )
```

---

# Dry Run

Input:

```python
fib(4)
```

---

```text
fib(4)

= fib(3) + fib(2)

------------------

fib(3)

= fib(2) + fib(1)

------------------

fib(2)

= fib(1) + fib(0)
```

Tree:

```text
            fib(4)
           /      \
      fib(3)     fib(2)
      /    \      /   \
 fib(2) fib(1) fib(1) fib(0)
  / \
fib(1) fib(0)
```

Result:

```text
3
```

---

# Why Is This Slow?

Notice:

```text
fib(2)
```

is calculated:

```text
Multiple Times
```

Same for:

```text
fib(1)
fib(0)
```

Huge amount of repeated work.

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(2ⁿ) |
| Space | O(n) |

---

### Why O(2ⁿ)?

Every call generates:

```text
Two More Calls
```

Roughly:

```text
1

2

4

8

16
```

calls per level.

Exponential growth.

---

### Why O(n) Space?

Maximum recursion depth:

```text
n
```

because:

```text
fib(n)
→ fib(n-1)
→ fib(n-2)
...
```

is stored in the call stack.

---

# Better Approach (Dynamic Programming)

Store previously computed answers.

---

## Python

```python
class Solution:
    def fib(self, n):

        if n <= 1:
            return n

        dp = [0] * (n + 1)

        dp[1] = 1

        for i in range(2, n + 1):

            dp[i] = (
                dp[i - 1]
                +
                dp[i - 2]
            )

        return dp[n]
```

---

# Complexity

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(n) |

Much better.

---

# Best Approach (Space Optimized)

We only need:

```text
Previous Two Values
```

---

## Python

```python
class Solution:
    def fib(self, n):

        if n <= 1:
            return n

        a = 0
        b = 1

        for _ in range(2, n + 1):

            a, b = b, a + b

        return b
```

---

# Dry Run

Input:

```python
n = 5
```

---

Initial:

```text
a = 0
b = 1
```

---

Iteration 1

```text
1
1
```

---

Iteration 2

```text
1
2
```

---

Iteration 3

```text
2
3
```

---

Iteration 4

```text
3
5
```

Answer:

```python
5
```

---

# Complexity

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(1) |

Best solution.

---

# Visualization

```text
0 1

0+1 = 1

1+1 = 2

1+2 = 3

2+3 = 5
```

---

# Interview Insight

This is one of the most important recursion examples.

It teaches:

```text
Overlapping Subproblems
```

which leads directly to:

```text
Dynamic Programming
```

---

# Pattern Recognition

Whenever you see:

- Repeated Recursive Calls
- Same Inputs Computed Again
- Exponential Recursion

Think:

```text
Memoization

or

Dynamic Programming
```

---

# Common Mistakes

## Mistake 1

Missing base case.

Wrong:

```python
return fib(n-1) + fib(n-2)
```

Infinite recursion.

---

## Mistake 2

Thinking recursion is always optimal.

Recursive Fibonacci is elegant.

But:

```text
Very Slow
```

---

## Mistake 3

Using recursion for huge:

```python
n = 1000
```

May cause stack overflow.

---

# Recursion Cheat Sheet

```python
if n <= 1:
    return n

return fib(n-1) + fib(n-2)
```

---

# Key Takeaways

✅ Fibonacci is a classic recursion problem

✅ Needs a base case

✅ Recursive solution is O(2ⁿ)

✅ Many repeated calculations

✅ Dynamic Programming improves to O(n)

✅ Space optimization improves to O(1)

✅ Foundation of DP

---

# Related Problems

1. Climbing Stairs (#70)
2. House Robber (#198)
3. Min Cost Climbing Stairs (#746)
4. Tribonacci Number (#1137)
5. Decode Ways (#91)

These all build on Fibonacci-style thinking.

---

# Golden Rule Learned

```text
Recursive Calls
Repeat Same Work?
        ↓
Use Dynamic Programming
```

Fibonacci is the gateway problem that teaches the transition from **Recursion → Dynamic Programming**.
