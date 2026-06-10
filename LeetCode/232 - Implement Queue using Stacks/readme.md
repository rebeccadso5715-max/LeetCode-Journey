# LeetCode #232 — Implement Queue using Stacks

**Difficulty:** Easy

---

# Problem

Implement a Queue using Stacks.

The queue should support:

```text
push(x)
pop()
peek()
empty()
```

A queue follows:

```text
FIFO

First In
First Out
```

But a stack follows:

```text
LIFO

Last In
First Out
```

We must use stacks to create queue behavior.

---

# Core Idea

Use two stacks:

```text
Input Stack
Output Stack
```

---

# Why Two Stacks?

Input Stack:

```text
Used for push operations.
```

Output Stack:

```text
Used for pop operations.
```

When Output Stack is empty:

```text
Move everything

Input → Output
```

This reverses the order.

---

# Visualization

Push:

```text
1
2
3
```

Input Stack:

```text
Top
 ↓

3
2
1
```

Output Stack:

```text
Empty
```

---

Need:

```text
Pop
```

Move:

```text
Input → Output
```

Result:

Output Stack:

```text
Top
 ↓

1
2
3
```

Now:

```text
Pop → 1
```

FIFO achieved.

---

# Example

Operations:

```python
push(1)
push(2)
peek()
pop()
empty()
```

---

### push(1)

Input:

```text
1
```

---

### push(2)

Input:

```text
2
1
```

---

### peek()

Output empty.

Transfer:

```text
Input → Output
```

Output:

```text
1
2
```

Front:

```python
1
```

---

### pop()

Remove:

```python
1
```

Output:

```text
2
```

---

### empty()

Not empty.

Return:

```python
False
```

---

# Python Solution

```python
class MyQueue:

    def __init__(self):

        self.input = []
        self.output = []

    def push(self, x):

        self.input.append(x)

    def pop(self):

        self.peek()

        return self.output.pop()

    def peek(self):

        if not self.output:

            while self.input:

                self.output.append(
                    self.input.pop()
                )

        return self.output[-1]

    def empty(self):

        return (
            len(self.input) == 0 and
            len(self.output) == 0
        )
```

---

# Dry Run

### push(1)

```text
Input

1

Output

Empty
```

---

### push(2)

```text
Input

2
1
```

---

### peek()

Move:

```text
Input → Output
```

Output:

```text
1
2
```

Front:

```python
1
```

---

### pop()

Remove:

```python
1
```

Output:

```text
2
```

---

### push(3)

Input:

```text
3
```

Output:

```text
2
```

---

### pop()

Output already has data.

Remove:

```python
2
```

No transfer needed.

---

# Why Does This Work?

Input Stack:

```text
Newest element on top.
```

When transferred:

```text
Order reverses.
```

Example:

```text
Input

3
2
1
```

Transfer:

```text
Output

1
2
3
```

Now:

```text
Oldest element is on top.
```

Exactly what a queue needs.

---

# Amortized Analysis

At first glance:

```python
while self.input:
```

looks expensive.

---

But:

Each element:

```text
Moves from Input → Output
only once.
```

Therefore:

```text
Total Work = O(n)
```

over all operations.

---

Average per operation:

```text
O(1) amortized
```

---

# Complexity Analysis

| Operation | Complexity |
|------------|------------|
| Push | O(1) |
| Pop | O(1) amortized |
| Peek | O(1) amortized |
| Empty | O(1) |

---

# Java Solution

```java
import java.util.Stack;

class MyQueue {

    Stack<Integer> input;
    Stack<Integer> output;

    public MyQueue() {

        input = new Stack<>();
        output = new Stack<>();
    }

    public void push(int x) {

        input.push(x);
    }

    public int pop() {

        peek();

        return output.pop();
    }

    public int peek() {

        if(output.isEmpty()) {

            while(!input.isEmpty()) {

                output.push(
                    input.pop()
                );
            }
        }

        return output.peek();
    }

    public boolean empty() {

        return input.isEmpty()
            && output.isEmpty();
    }
}
```

---

# Interview Insight

This problem teaches:

```text
Data Structure Transformation
```

We convert:

```text
LIFO
```

into:

```text
FIFO
```

using two stacks.

---

# Pattern Recognition

Whenever you hear:

- Implement Queue
- Using Stacks
- Reverse Order
- Transfer Elements

Think:

```text
Two Stacks
```

---

# Common Mistakes

## Mistake 1

Moving elements every time.

Wrong:

```python
pop():
    move everything
```

This makes operations slow.

Only transfer when:

```python
output is empty
```

---

## Mistake 2

Using one stack.

One stack cannot efficiently simulate FIFO behavior.

---

## Mistake 3

Forgetting to call:

```python
peek()
```

inside:

```python
pop()
```

to ensure Output Stack is ready.

---

# Two-Stack Queue Cheat Sheet

```python
push:
    input.append(x)

peek/pop:

    if output empty:

        move all
        input → output
```

---

# Key Takeaways

✅ Queue = FIFO

✅ Stack = LIFO

✅ Use two stacks

✅ Input stack handles pushes

✅ Output stack handles pops

✅ Transfer only when output is empty

✅ O(1) amortized operations

✅ Classic data structure design problem

---

# Related Problems

1. Implement Stack using Queues (#225)
2. Min Stack (#155)
3. Baseball Game (#682)
4. Valid Parentheses (#20)

These strengthen data structure fundamentals.

---

# Golden Rule Learned

```text
Need Queue Behavior
Using Stacks?
        ↓
Use Two Stacks
```

One stack stores incoming elements, while the other reverses their order to achieve FIFO behavior.
