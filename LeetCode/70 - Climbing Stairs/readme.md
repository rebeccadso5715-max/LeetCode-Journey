# LeetCode #70 — Climbing Stairs

**Difficulty:** Easy

---

# Problem

You are climbing a staircase.

Each time you can climb:

```text
1 step
or
2 steps
```

Find the number of distinct ways to reach the top.

---

## Example 1

### Input

```python
n = 2
```

### Output

```python
2
```

Ways:

```text
1 + 1

2
```

---

## Example 2

### Input

```python
n = 3
```

### Output

```python
3
```

Ways:

```text
1 + 1 + 1

1 + 2

2 + 1
```

---

# Key Observation

Suppose:

```python
n = 5
```

How can we reach step 5?

---

### Option 1

Come from:

```text
Step 4
```

using:

```text
1 step
```

---

### Option 2

Come from:

```text
Step 3
```

using:

```text
2 steps
```

---

Therefore:

```text
Ways to reach step 5

=

Ways to reach step 4

+

Ways to reach step 3
```

---

# Recurrence Relation

:contentReference[oaicite:0]{index=0}

Base cases:

```text
f(1) = 1

f(2) = 2
```

---

# Why Does This Look Familiar?

Compare with Fibonacci:

```text
Fib(n)

=
Fib(n-1)
+
Fib(n-2)
```

Climbing Stairs is essentially:

```text
Fibonacci Pattern
```

---

# Recursive Solution

## Python

```python
class Solution:
    def climbStairs(self, n):

        if n <= 2:
            return n

        return (
            self.climbStairs(n - 1)
            +
            self.climbStairs(n - 2)
        )
```

---

# Dry Run

Input:

```python
n = 4
```

---

```text
climb(4)

=
climb(3)
+
climb(2)
```

---

```text
climb(3)

=
climb(2)
+
climb(1)
```

---

Tree:

```text
           climb(4)
           /      \
      climb(3)   climb(2)
       /    \
 climb(2) climb(1)
```

Answer:

```text
5
```

Ways:

```text
1+1+1+1

1+1+2

1+2+1

2+1+1

2+2
```

---

# Problem with Recursion

Notice:

```text
climb(2)
```

is calculated multiple times.

Repeated work.

---

# Complexity

| Metric | Complexity |
|----------|------------|
| Time | O(2ⁿ) |
| Space | O(n) |

Too slow.

---

# Dynamic Programming Solution

Store previous answers.

---

## Python

```python
class Solution:
    def climbStairs(self, n):

        if n <= 2:
            return n

        dp = [0] * (n + 1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):

            dp[i] = (
                dp[i - 1]
                +
                dp[i - 2]
            )

        return dp[n]
```

---

# DP Visualization

```text
n = 5

dp[1] = 1

dp[2] = 2

dp[3] = 3

dp[4] = 5

dp[5] = 8
```

---

# Complexity

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(n) |

---

# Optimal Solution (Space Optimized)

Only previous two values matter.

---

## Python

```python
class Solution:
    def climbStairs(self, n):

        if n <= 2:
            return n

        a = 1
        b = 2

        for _ in range(3, n + 1):

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
a = 1
b = 2
```

---

Step 3

```text
1 2

↓

2 3
```

---

Step 4

```text
2 3

↓

3 5
```

---

Step 5

```text
3 5

↓

5 8
```

Answer:

```python
8
```

---

# Complexity

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(1) |

Best solution.

---

# Java Solution

```java
class Solution {

    public int climbStairs(int n) {

        if(n <= 2)
            return n;

        int a = 1;
        int b = 2;

        for(int i = 3; i <= n; i++) {

            int temp = a + b;

            a = b;
            b = temp;
        }

        return b;
    }
}
```

---

# Interview Insight

This is one of the most famous Dynamic Programming problems.

The key realization:

```text
Current Answer
Depends On
Previous Two Answers
```

Exactly like Fibonacci.

---

# Pattern Recognition

Whenever you hear:

- Number of Ways
- Count Possibilities
- Steps
- Paths
- Choices at Each Position

Think:

```text
Dynamic Programming
```

---

# Common Mistakes

## Mistake 1

Using plain recursion.

```text
Too Slow
```

---

## Mistake 2

Wrong base cases.

Correct:

```python
f(1) = 1

f(2) = 2
```

---

## Mistake 3

Building full DP array when only two values are needed.

Use:

```python
a
b
```

instead.

---

# DP Cheat Sheet

```python
a = 1
b = 2

for i in range(3, n + 1):

    a, b = b, a + b

return b
```

---

# Key Takeaways

✅ Climbing Stairs follows Fibonacci pattern

✅ Recurrence:

```text
f(n)=f(n-1)+f(n-2)
```

✅ Recursive solution is O(2ⁿ)

✅ DP improves to O(n)

✅ Space optimization improves to O(1)

✅ One of the most important beginner DP problems

---

# Related Problems

1. Fibonacci Number (#509)
2. Min Cost Climbing Stairs (#746)
3. House Robber (#198)
4. Decode Ways (#91)
5. Tribonacci Number (#1137)

All use similar DP thinking.

---

# Golden Rule Learned

```text
Current Answer
Depends On Previous Answers?
         ↓
Use Dynamic Programming
```

Climbing Stairs is often considered the first true Dynamic Programming problem and is the perfect bridge from Recursion to DP.
