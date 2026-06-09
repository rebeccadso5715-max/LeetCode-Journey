# LeetCode #121 — Best Time to Buy and Sell Stock

**Difficulty:** Easy

---

# Problem

You are given an array `prices`.

```python
prices[i]
```

represents the stock price on day `i`.

You want to:

1. Buy one stock.
2. Sell one stock later.

Return the maximum profit possible.

If no profit is possible:

```python
return 0
```

---

## Example

### Input

```python
prices = [7,1,5,3,6,4]
```

### Output

```python
5
```

### Explanation

Buy:

```text
Day 2 → Price = 1
```

Sell:

```text
Day 5 → Price = 6
```

Profit:

```text
6 - 1 = 5
```

---

# Key Observation

We must:

```text
Buy First
Sell Later
```

This means:

```text
Buy Day < Sell Day
```

We cannot sell before buying.

---

# Brute Force Approach

Try every buy day.

For each buy day:

Try every future sell day.

---

## Python Solution

```python
class Solution:
    def maxProfit(self, prices):

        profit = 0

        for i in range(len(prices)):

            for j in range(i + 1, len(prices)):

                profit = max(
                    profit,
                    prices[j] - prices[i]
                )

        return profit
```

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n²) |
| Space | O(1) |

### Why O(n²)?

For every buy day:

```text
Check all future sell days
```

Nested loops.

---

# Optimal Approach (Two Pointers)

Use:

```python
left = buy day
right = sell day
```

Visualization:

```text
Buy       Sell

7  1  5  3  6  4
↑  ↑
L  R
```

---

## Core Idea

If:

```python
prices[right] > prices[left]
```

profit exists.

Calculate:

```python
prices[right] - prices[left]
```

Update maximum profit.

---

If:

```python
prices[right] <= prices[left]
```

we found a cheaper buying day.

Move:

```python
left = right
```

because buying at a lower price is always better.

---

## Python Solution

```python
class Solution:
    def maxProfit(self, prices):

        left = 0
        right = 1

        profit = 0

        while right < len(prices):

            if prices[right] > prices[left]:

                profit = max(
                    profit,
                    prices[right] - prices[left]
                )

            else:
                left = right

            right += 1

        return profit
```

---

# Dry Run

Input:

```python
[7,1,5,3,6,4]
```

Initial:

```python
left = 0
right = 1
profit = 0
```

---

### Day 1

```python
7 → Buy
1 → Sell
```

Profit:

```python
1 - 7 = -6
```

Not useful.

Better buy price found:

```python
left = 1
```

---

### Day 2

```python
Buy = 1
Sell = 5
```

Profit:

```python
5 - 1 = 4
```

Update:

```python
profit = 4
```

---

### Day 3

```python
Buy = 1
Sell = 3
```

Profit:

```python
2
```

No improvement.

---

### Day 4

```python
Buy = 1
Sell = 6
```

Profit:

```python
5
```

Update:

```python
profit = 5
```

---

### Day 5

```python
Buy = 1
Sell = 4
```

Profit:

```python
3
```

No improvement.

---

### Final Answer

```python
5
```

---

# Visualization

```text
Prices

7  1  5  3  6  4
↑
Buy

Cheaper price found

7  1  5  3  6  4
   ↑
 Buy

Profit Candidates

1 → 5 = 4

1 → 3 = 2

1 → 6 = 5  ← Best

1 → 4 = 3
```

---

# Alternative View

Keep track of:

```text
Minimum Price Seen So Far
```

Then calculate:

```text
Current Price - Minimum Price
```

This is the same idea.

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(1) |

### Why O(n)?

Each price is processed once.

---

### Why O(1) Space?

Only a few variables:

```python
left
right
profit
```

---

# Java Solution

```java
class Solution {

    public int maxProfit(int[] prices) {

        int left = 0;
        int right = 1;

        int profit = 0;

        while(right < prices.length) {

            if(prices[right] > prices[left]) {

                profit = Math.max(
                    profit,
                    prices[right] - prices[left]
                );
            }

            else {
                left = right;
            }

            right++;
        }

        return profit;
    }
}
```

---

# Interview Insight

This problem looks like a stock problem.

But the real pattern is:

```text
Two Pointers
```

We maintain:

```text
Best Buy Price So Far
```

and

```text
Current Sell Price
```

---

# Pattern Recognition

Whenever you hear:

- Buy then Sell
- Max Profit
- Minimum Before Maximum
- Best Pair Order

Think:

```text
Two Pointers
```

or

```text
Track Minimum So Far
```

---

# Key Takeaways

✅ Buy must happen before sell

✅ Keep the cheapest buying day

✅ Calculate profit for each future day

✅ Update maximum profit

✅ O(n) time

✅ O(1) space

✅ Classic interview favorite

---

# Related Problems

1. Best Time to Buy and Sell Stock II
2. Best Time to Buy and Sell Stock III
3. Best Time to Buy and Sell Stock with Cooldown
4. Maximum Subarray
5. Container With Most Water

These all involve optimization while scanning an array.

---

# Golden Rule Learned

```text
Need Maximum Profit?
        ↓
Track Minimum Value
Seen So Far
```

This is one of the most important optimization patterns in array problems.
