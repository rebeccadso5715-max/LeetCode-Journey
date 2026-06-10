# LeetCode #682 — Baseball Game

**Difficulty:** Easy

---

# Problem

You are given a list of operations.

Each operation represents a score.

Calculate the total score after processing all operations.

---

## Operations

### Integer

```python
"5"
```

Add score:

```python
5
```

---

### "C"

Cancel previous score.

Example:

```python
["5", "C"]
```

Result:

```text
[]
```

---

### "D"

Double previous score.

Example:

```python
["5", "D"]
```

Result:

```text
[5, 10]
```

---

### "+"

Add last two scores.

Example:

```python
["5", "2", "+"]
```

Result:

```text
[5, 2, 7]
```

because:

```text
5 + 2 = 7
```

---

# Example

### Input

```python
operations = ["5","2","C","D","+"]
```

### Output

```python
30
```

---

# Dry Run

Start:

```python
stack = []
```

---

### Operation = "5"

Push:

```python
[5]
```

---

### Operation = "2"

Push:

```python
[5, 2]
```

---

### Operation = "C"

Remove previous score.

```python
[5]
```

---

### Operation = "D"

Double previous score.

```python
2 * 5 = 10
```

Push:

```python
[5, 10]
```

---

### Operation = "+"

Sum last two scores.

```python
5 + 10 = 15
```

Push:

```python
[5, 10, 15]
```

---

### Final Score

```python
5 + 10 + 15
=
30
```

Answer:

```python
30
```

---

# Key Observation

Every operation depends on:

```text
Most Recent Scores
```

Examples:

```text
"C" → Last Score

"D" → Last Score

"+" → Last Two Scores
```

This is a huge clue.

Think:

```text
Stack
```

---

# Why Stack?

Stack follows:

```text
LIFO

Last In
First Out
```

The most recent score is always on top.

---

# Stack Visualization

```text
Top
 ↓

15
10
5
```

Access:

```python
stack[-1]
```

Most recent score.

---

# Optimal Approach

Maintain a stack.

Process each operation.

---

## Python Solution

```python
class Solution:
    def calPoints(self, operations):

        stack = []

        for op in operations:

            if op == "C":

                stack.pop()

            elif op == "D":

                stack.append(
                    2 * stack[-1]
                )

            elif op == "+":

                stack.append(
                    stack[-1] +
                    stack[-2]
                )

            else:

                stack.append(
                    int(op)
                )

        return sum(stack)
```

---

# Visualization

Input:

```python
["5","2","C","D","+"]
```

---

### Push 5

```text
5
```

---

### Push 2

```text
2
5
```

---

### C

Pop 2

```text
5
```

---

### D

Push 10

```text
10
5
```

---

### +

Push:

```text
10 + 5 = 15
```

```text
15
10
5
```

---

Final:

```python
sum(stack)
=
30
```

---

# Why Does This Work?

Every operation only cares about:

```text
Recent Scores
```

A stack gives instant access to:

```python
stack[-1]
stack[-2]
```

which makes all operations O(1).

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(n) |

### Why O(n)?

Each operation is processed once.

---

### Why O(n) Space?

Stack may store all scores.

---

# Java Solution

```java
import java.util.Stack;

class Solution {

    public int calPoints(
        String[] operations
    ) {

        Stack<Integer> stack =
            new Stack<>();

        for(String op : operations) {

            if(op.equals("C")) {

                stack.pop();
            }

            else if(op.equals("D")) {

                stack.push(
                    2 * stack.peek()
                );
            }

            else if(op.equals("+")) {

                int top = stack.pop();

                int sum =
                    top + stack.peek();

                stack.push(top);

                stack.push(sum);
            }

            else {

                stack.push(
                    Integer.parseInt(op)
                );
            }
        }

        int score = 0;

        for(int num : stack) {
            score += num;
        }

        return score;
    }
}
```

---

# Interview Insight

This is one of the easiest Stack problems.

The key realization:

```text
Need Access To
Recent Elements
        ↓
Use Stack
```

---

# Pattern Recognition

Whenever you hear:

- Undo
- Cancel
- Previous Operation
- Most Recent Element
- Last Two Elements

Think:

```text
Stack
```

---

# Common Mistakes

## Mistake 1

Using:

```python
stack[-1]
```

without checking if stack exists.

---

## Mistake 2

Confusing:

```python
"C"
```

with setting value to zero.

It means:

```python
Remove Previous Score
```

---

## Mistake 3

Forgetting:

```python
int(op)
```

for numeric strings.

---

# Stack Cheat Sheet

```python
stack.append(x)   # Push

stack.pop()       # Pop

stack[-1]         # Top

len(stack)        # Size
```

---

# Key Takeaways

✅ Operations depend on recent scores

✅ Stack stores score history

✅ "C" → Pop

✅ "D" → Double top

✅ "+" → Sum last two

✅ O(n) time

✅ O(n) space

✅ Classic Stack problem

---

# Related Problems

1. Valid Parentheses (#20)
2. Min Stack (#155)
3. Backspace String Compare (#844)
4. Daily Temperatures (#739)
5. Next Greater Element (#496)

All heavily use stacks.

---

# Golden Rule Learned

```text
Need Recent History?
        ↓
Use Stack
```

Baseball Game is often the first problem people solve when learning Stack-based thinking.
