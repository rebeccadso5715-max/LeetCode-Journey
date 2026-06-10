# LeetCode #155 — Min Stack

**Difficulty:** Medium

---

# Problem

Design a stack that supports:

```python
push(val)
pop()
top()
getMin()
```

All operations must work in:

```text
O(1)
```

time.

---

# Example

```python
MinStack minStack = new MinStack();

minStack.push(-2);
minStack.push(0);
minStack.push(-3);

minStack.getMin();
```

Output:

```python
-3
```

---

```python
minStack.pop();

minStack.top();
```

Output:

```python
0
```

---

```python
minStack.getMin();
```

Output:

```python
-2
```

---

# Why Is This Problem Tricky?

Normal Stack:

```python
push()
pop()
top()
```

are already O(1).

---

But:

```python
getMin()
```

is difficult.

If we scan the entire stack:

```python
min(stack)
```

Complexity:

```text
O(n)
```

Not allowed.

---

# Brute Force Idea

Store elements normally.

Whenever:

```python
getMin()
```

is called:

```python
return min(stack)
```

---

## Complexity

| Operation | Complexity |
|------------|------------|
| Push | O(1) |
| Pop | O(1) |
| Top | O(1) |
| GetMin | O(n) |

Fails requirement.

---

# Optimal Idea

Maintain:

```text
1. Normal Stack
2. Min Stack
```

---

# Visualization

Normal Stack:

```text
Top
 ↓

8
2
5
```

---

Min Stack:

```text
Top
 ↓

2
2
5
```

Notice:

```text
Each position stores
minimum so far.
```

---

# Example

Push:

```python
5
```

Stack:

```text
[5]
```

MinStack:

```text
[5]
```

---

Push:

```python
2
```

Minimum:

```python
min(5,2) = 2
```

Stack:

```text
[5,2]
```

MinStack:

```text
[5,2]
```

---

Push:

```python
8
```

Minimum:

```python
min(2,8) = 2
```

Stack:

```text
[5,2,8]
```

MinStack:

```text
[5,2,2]
```

---

# Key Insight

Top of MinStack always stores:

```text
Current Minimum
```

Therefore:

```python
getMin()
```

becomes:

```python
return minStack[-1]
```

Complexity:

```text
O(1)
```

---

# Python Solution

```python
class MinStack:

    def __init__(self):

        self.stack = []
        self.minStack = []

    def push(self, val):

        self.stack.append(val)

        if not self.minStack:
            self.minStack.append(val)

        else:
            self.minStack.append(
                min(val,
                    self.minStack[-1])
            )

    def pop(self):

        self.stack.pop()
        self.minStack.pop()

    def top(self):

        return self.stack[-1]

    def getMin(self):

        return self.minStack[-1]
```

---

# Dry Run

### push(5)

```text
Stack

[5]

MinStack

[5]
```

---

### push(2)

```text
Stack

[5,2]

MinStack

[5,2]
```

---

### push(8)

```text
Stack

[5,2,8]

MinStack

[5,2,2]
```

---

### getMin()

```python
return 2
```

Top of MinStack:

```text
2
```

---

### pop()

Remove:

```text
8
```

Stack:

```text
[5,2]
```

MinStack:

```text
[5,2]
```

---

### getMin()

```python
2
```

Still correct.

---

# Visualization

```text
Stack       MinStack

5           5

5 2         5 2

5 2 8       5 2 2

5 2 8 1     5 2 2 1
```

Current minimum:

```text
Top of MinStack
```

---

# Why Does This Work?

Every time we push:

```python
min(
    current_value,
    previous_min
)
```

Thus:

```text
MinStack[i]
```

stores:

```text
Minimum among first i elements
```

---

# Complexity Analysis

| Operation | Complexity |
|------------|------------|
| Push | O(1) |
| Pop | O(1) |
| Top | O(1) |
| GetMin | O(1) |

---

# Java Solution

```java
import java.util.Stack;

class MinStack {

    Stack<Integer> stack;
    Stack<Integer> minStack;

    public MinStack() {

        stack = new Stack<>();
        minStack = new Stack<>();
    }

    public void push(int val) {

        stack.push(val);

        if(minStack.isEmpty()) {
            minStack.push(val);
        }

        else {
            minStack.push(
                Math.min(
                    val,
                    minStack.peek()
                )
            );
        }
    }

    public void pop() {

        stack.pop();
        minStack.pop();
    }

    public int top() {

        return stack.peek();
    }

    public int getMin() {

        return minStack.peek();
    }
}
```

---

# Interview Insight

This problem teaches:

```text
Auxiliary Stack
```

An extra stack storing useful information.

---

# Pattern Recognition

Whenever you hear:

- Current Minimum
- Current Maximum
- Running Minimum
- Running Maximum
- O(1) Query

Think:

```text
Extra Stack
```

---

# Common Mistakes

## Mistake 1

Using:

```python
min(stack)
```

inside:

```python
getMin()
```

Complexity becomes:

```text
O(n)
```

---

## Mistake 2

Forgetting to pop from:

```python
minStack
```

when popping from stack.

Both stacks must stay synchronized.

---

## Mistake 3

Storing only new minimums.

This complicates pop operations.

Store:

```python
Current minimum
for every position.
```

---

# Min Stack Cheat Sheet

```python
stack.append(val)

minStack.append(
    min(val,
        minStack[-1])
)
```

Current minimum:

```python
minStack[-1]
```

---

# Key Takeaways

✅ Use two stacks

✅ One stores values

✅ One stores minimums

✅ Top of MinStack = current minimum

✅ All operations become O(1)

✅ Classic Stack Design problem

---

# Related Problems

1. Baseball Game (#682)
2. Valid Parentheses (#20)
3. Daily Temperatures (#739)
4. Largest Rectangle in Histogram (#84)
5. Online Stock Span (#901)

These all use Stack-based thinking.

---

# Golden Rule Learned

```text
Need O(1)
Min/Max Query?
      ↓
Maintain Extra Data
Alongside Stack
```

Min Stack is one of the most important **Stack Design** interview problems and introduces the idea of storing additional information to achieve constant-time operations.
