# LeetCode #225 — Implement Stack using Queues

**Difficulty:** Easy

---

# Problem

Implement a Stack using Queues.

The stack should support:

```text
push(x)
pop()
top()
empty()
```

A stack follows:

```text
LIFO

Last In First Out
```

But a queue follows:

```text
FIFO

First In First Out
```

So we need to make a Queue behave like a Stack.

---

# Core Idea

Queue behaves:

```text
FIFO
```

But we need:

```text
LIFO
```

So after every insertion, rotate the queue.

That means:

```text
New element should come to the front.
```

---

# Example

Push:

```text
1
2
3
```

Normal Queue:

```text
Front → 1 2 3
```

But Stack needs:

```text
Top → 3 2 1
```

So after inserting `3`, rotate old elements behind it.

---

# Optimal Approach

Use one queue.

After pushing a new element:

1. Add it to the queue.
2. Rotate all previous elements behind it.

---

# Python Solution

```python
from collections import deque

class MyStack:

    def __init__(self):

        self.q = deque()

    def push(self, x):

        self.q.append(x)

        for i in range(len(self.q) - 1):

            self.q.append(
                self.q.popleft()
            )

    def pop(self):

        return self.q.popleft()

    def top(self):

        return self.q[0]

    def empty(self):

        return len(self.q) == 0
```

---

# Dry Run

### push(1)

Add:

```text
[1]
```

No rotation needed.

Stack top:

```text
1
```

---

### push(2)

Add:

```text
[1, 2]
```

Rotate old elements:

```text
[2, 1]
```

Stack top:

```text
2
```

---

### push(3)

Add:

```text
[2, 1, 3]
```

Rotate old elements:

```text
[1, 3, 2]
```

Then:

```text
[3, 2, 1]
```

Stack top:

```text
3
```

---

# Visualization

```text
push(1)

Queue:
Front → 1

----------------

push(2)

Before Rotation:
Front → 1 2

After Rotation:
Front → 2 1

----------------

push(3)

Before Rotation:
Front → 2 1 3

After Rotation:
Front → 3 2 1
```

Now queue front behaves like stack top.

---

# Why Does This Work?

After every push:

```text
Newest element
is moved to the front.
```

So:

```python
popleft()
```

removes the newest element.

That is exactly:

```text
LIFO
```

---

# Complexity Analysis

| Operation | Complexity |
|------------|------------|
| Push | O(n) |
| Pop | O(1) |
| Top | O(1) |
| Empty | O(1) |

---

### Why Push is O(n)?

After inserting, we rotate all previous elements.

---

### Why Pop is O(1)?

The newest element is always at the front.

So:

```python
popleft()
```

is instant.

---

# Java Solution

```java
import java.util.Queue;
import java.util.LinkedList;

class MyStack {

    Queue<Integer> q;

    public MyStack() {

        q = new LinkedList<>();
    }

    public void push(int x) {

        q.offer(x);

        int size = q.size();

        for(int i = 0; i < size - 1; i++) {

            q.offer(q.poll());
        }
    }

    public int pop() {

        return q.poll();
    }

    public int top() {

        return q.peek();
    }

    public boolean empty() {

        return q.isEmpty();
    }
}
```

---

# Interview Insight

This problem teaches how to convert:

```text
FIFO behavior
```

into:

```text
LIFO behavior
```

by rearranging the queue after insertion.

---

# Pattern Recognition

Whenever you hear:

- Implement Stack
- Using Queue
- Convert FIFO to LIFO
- Rotate Elements

Think:

```text
Queue Rotation
```

---

# Common Mistakes

## Mistake 1

Forgetting to rotate after push.

Then queue remains FIFO.

---

## Mistake 2

Using:

```python
pop()
```

on deque.

For queue behavior, use:

```python
popleft()
```

---

## Mistake 3

Rotating wrong number of times.

Correct:

```python
len(self.q) - 1
```

because the newly added element should stay in front after rotation.

---

# Key Takeaways

✅ Queue follows FIFO

✅ Stack needs LIFO

✅ Rotate queue after every push

✅ Newest element becomes front

✅ Push takes O(n)

✅ Pop takes O(1)

✅ Classic queue-design problem

---

# Related Problems

1. Implement Queue using Stacks (#232)
2. Min Stack (#155)
3. Baseball Game (#682)
4. Valid Parentheses (#20)

All help build strong data-structure design intuition.

---

# Golden Rule Learned

```text
Need Stack Behavior
Using Queue?
        ↓
Push Then Rotate
```

This trick converts FIFO into LIFO.
