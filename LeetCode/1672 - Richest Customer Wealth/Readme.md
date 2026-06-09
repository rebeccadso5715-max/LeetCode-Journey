# LeetCode #1672 — Richest Customer Wealth

**Difficulty:** Easy

---

# Problem

You are given a 2D array `accounts` where:

- Each row represents a customer.
- Each column represents money in a bank account.

Return the wealth of the richest customer.

---

## Example

### Input

```python
accounts = [
    [1, 2, 3],
    [3, 2, 1]
]
```

### Output

```python
6
```

### Explanation

Customer 1:

```text
1 + 2 + 3 = 6
```

Customer 2:

```text
3 + 2 + 1 = 6
```

Richest Wealth:

```text
6
```

---

# Approach

For each customer:

1. Calculate total wealth.
2. Compare with current maximum wealth.
3. Update the maximum if necessary.

---

# Python Solution

```python
class Solution:
    def maximumWealth(self, accounts):

        richest = 0

        for customer in accounts:

            wealth = sum(customer)

            richest = max(richest, wealth)

        return richest
```

---

# Dry Run

Input:

```python
accounts = [
    [1, 2, 3],
    [3, 2, 1]
]
```

### Customer 1

```python
wealth = 1 + 2 + 3 = 6

richest = max(0, 6)

richest = 6
```

### Customer 2

```python
wealth = 3 + 2 + 1 = 6

richest = max(6, 6)

richest = 6
```

### Final Answer

```python
6
```

---

# Complexity Analysis

Let:

- m = number of customers (rows)
- n = number of bank accounts per customer (columns)

| Metric | Complexity |
|----------|------------|
| Time | O(m × n) |
| Space | O(1) |

### Why O(m × n)?

Every element of the matrix is visited exactly once.

### Why O(1) Space?

Only a few variables are used regardless of input size.

---

# Java Solution

```java
class Solution {

    public int maximumWealth(int[][] accounts) {

        int richest = 0;

        for(int[] customer : accounts) {

            int wealth = 0;

            for(int money : customer) {
                wealth += money;
            }

            richest = Math.max(richest, wealth);
        }

        return richest;
    }
}
```

---

# Alternative Python Solution

Using a one-liner:

```python
class Solution:
    def maximumWealth(self, accounts):
        return max(sum(customer) for customer in accounts)
```

---

# Interview Insight

This problem teaches:

## 1. 2D Arrays

A 2D array is an array of arrays.

Example:

```python
accounts = [
    [1, 2, 3],
    [3, 2, 1]
]
```

Visualization:

```text
Row 0 → [1, 2, 3]
Row 1 → [3, 2, 1]
```

---

## 2. Row Traversal

We process one row at a time.

```python
for customer in accounts:
```

This is a very common pattern in matrix problems.

---

## 3. Aggregation

Aggregation means combining values into a single result.

Examples:

- Sum
- Maximum
- Minimum
- Average
- Count

In this problem:

```python
wealth = sum(customer)
```

We aggregate all bank balances of a customer into one value.

---

# Key Takeaways

✅ Introduction to 2D arrays

✅ Learn row-wise traversal

✅ Practice aggregation (sum of elements)

✅ Track a running maximum

✅ Common matrix-processing interview pattern

---

# Pattern Recognition

When you hear:

- Richest Customer
- Maximum Sum Row
- Best Student
- Highest Score
- Largest Total

Think:

```text
Traverse each row
→ Calculate aggregate value
→ Track maximum
```

This pattern appears frequently in matrix and data-analysis interview questions.
