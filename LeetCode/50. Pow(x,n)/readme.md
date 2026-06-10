# LeetCode #50 — Pow(x, n)

**Difficulty:** Medium

---

# Problem

Implement:

```python
pow(x, n)
```

Calculate:

```text
xⁿ
```

without using built-in power functions.

---

## Example 1

### Input

```python
x = 2
n = 10
```

### Output

```python
1024
```

Because:

```text
2¹⁰ = 1024
```

---

## Example 2

### Input

```python
x = 2
n = 3
```

### Output

```python
8
```

Because:

```text
2 × 2 × 2 = 8
```

---

## Example 3

### Input

```python
x = 2
n = -2
```

### Output

```python
0.25
```

Because:

```text
2⁻²

=

1 / 2²

=

1 / 4

=

0.25
```

---

# Brute Force Approach

Multiply:

```text
x
```

by itself:

```text
n times
```

---

## Python

```python
class Solution:

    def myPow(self, x, n):

        result = 1

        for _ in range(abs(n)):

            result *= x

        if n < 0:
            return 1 / result

        return result
```

---

# Complexity

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(1) |

Too slow for large:

```python
n = 1_000_000
```

---

# Key Observation

Instead of:

```text
2¹⁰
=
2 × 2 × 2 × ...
```

we can use:

```text
2¹⁰

=

(2⁵)²
```

---

Similarly:

```text
2⁸

=

(2⁴)²
```

---

Each step:

```text
Cuts exponent in half
```

This is:

```text
Divide & Conquer
```

---

# Recurrence Relation

```text
power(x,n)

=
power(x,n/2)²
```

If:

```text
n is odd
```

then:

```text
power(x,n)

=
power(x,n/2)² × x
```

---

# Visualization

Compute:

```text
2¹⁰
```

---

```text
2¹⁰

↓

(2⁵)²

↓

((2²)² × 2)²

↓

((2¹)² × 2)²

↓

Answer
```

---

# Optimal Recursive Solution

## Python

```python
class Solution:

    def myPow(self, x, n):

        def power(x, n):

            if n == 0:
                return 1

            half = power(
                x,
                n // 2
            )

            if n % 2 == 0:

                return half * half

            return half * half * x

        if n < 0:

            return 1 / power(x, -n)

        return power(x, n)
```

---

# Dry Run

Input:

```python
x = 2
n = 10
```

---

```text
power(10)

↓

power(5)

↓

power(2)

↓

power(1)

↓

power(0)
```

Base case:

```python
1
```

---

Return:

```text
power(1)

=
1 × 1 × 2

=
2
```

---

```text
power(2)

=
2 × 2

=
4
```

---

```text
power(5)

=
4 × 4 × 2

=
32
```

---

```text
power(10)

=
32 × 32

=
1024
```

Answer:

```python
1024
```

---

# Why Is This Fast?

Instead of:

```text
n
```

recursive calls:

```text
10

9

8

7

...
```

we do:

```text
10

5

2

1

0
```

Exponent is halved every time.

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(log n) |
| Space | O(log n) |

---

### Why O(log n)?

Each recursive call:

```text
n → n/2
```

Number of levels:

```text
log₂(n)
```

---

### Why O(log n) Space?

Recursion depth:

```text
log₂(n)
```

stored in call stack.

---

# Handling Negative Powers

Example:

```text
2⁻³
```

Rule:

```text
x⁻ⁿ

=

1 / xⁿ
```

Therefore:

```python
if n < 0:

    return 1 / power(x, -n)
```

---

# Java Solution

```java
class Solution {

    public double myPow(
        double x,
        int n
    ) {

        long N = n;

        if(N < 0) {

            x = 1 / x;

            N = -N;
        }

        return power(x, N);
    }

    private double power(
        double x,
        long n
    ) {

        if(n == 0)
            return 1;

        double half =
            power(x, n / 2);

        if(n % 2 == 0)
            return half * half;

        return half * half * x;
    }
}
```

---

# Interview Insight

This problem introduces:

```text
Divide & Conquer
```

Instead of reducing:

```text
n by 1
```

we reduce:

```text
n by half
```

Huge speed improvement.

---

# Pattern Recognition

Whenever you hear:

- Power
- Exponentiation
- Fast Computation
- Repeated Squaring
- Divide & Conquer

Think:

```text
Binary Exponentiation
```

---

# Common Mistakes

## Mistake 1

Using:

```python
for i in range(n)
```

Too slow.

---

## Mistake 2

Forgetting negative powers.

```python
n < 0
```

must be handled separately.

---

## Mistake 3

Using:

```python
power(x, n-1)
```

instead of:

```python
power(x, n//2)
```

You lose the logarithmic improvement.

---

# Divide & Conquer Cheat Sheet

```python
half = power(
    x,
    n // 2
)

if n % 2 == 0:

    return half * half

return half * half * x
```

---

# Key Takeaways

✅ Uses Divide & Conquer

✅ Halves exponent every step

✅ Handles negative powers

✅ Much faster than brute force

✅ Time complexity O(log n)

✅ Space complexity O(log n)

✅ Classic Binary Exponentiation problem

---

# Related Problems

1. Sqrt(x) (#69)
2. Fibonacci Number (#509)
3. Climbing Stairs (#70)
4. Median of Two Sorted Arrays (#4)
5. Merge Sort

All use Divide & Conquer ideas.

---

# Golden Rule Learned

```text
Can Problem Size
Be Cut In Half?
       ↓
Use Divide & Conquer
```

Pow(x, n) is one of the most famous examples of **Binary Exponentiation**, a technique used heavily in competitive programming, mathematics, and interviews.
