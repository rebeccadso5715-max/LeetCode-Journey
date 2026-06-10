# Class 9 — Queues

## Why Queues Matter

Queues are one of the most important data structures in coding interviews.

Many graph, scheduling, and system-design problems rely heavily on queues.

Common interview topics include:

- Breadth First Search (BFS)
- Task Scheduling
- Sliding Window
- Level Order Traversal
- Producer Consumer Systems
- Message Queues

---

# What is a Queue?

A Queue follows:

```text
FIFO

First In
First Out
```

The first element inserted is the first element removed.

---

# Example

Operations:

```text
Enqueue 1
Enqueue 2
Enqueue 3
```

Queue:

```text
Front

1  2  3

        Rear
```

---

Removing elements:

```text
Dequeue → 1

Dequeue → 2

Dequeue → 3
```

---

# Visualization

```text
Enqueue 1

1

----------------

Enqueue 2

1 2

----------------

Enqueue 3

1 2 3

----------------

Dequeue

2 3

----------------

Dequeue

3
```

---

# Queue vs Stack

| Feature | Stack | Queue |
|----------|--------|--------|
| Order | LIFO | FIFO |
| Insert | Top | Rear |
| Remove | Top | Front |
| Example | Undo | Waiting Line |

---

# Real World Examples

## Printer Queue

Documents arrive:

```text
Doc1
Doc2
Doc3
```

Printing order:

```text
Doc1
Doc2
Doc3
```

First submitted:

```text
First printed
```

---

## Customer Service Line

```text
Customer A
Customer B
Customer C
```

Service order:

```text
A → B → C
```

FIFO.

---

## Task Scheduling

Operating systems often process tasks using queues.

```text
Task1
Task2
Task3
```

Executed in arrival order.

---

## Breadth First Search (BFS)

Graph:

```text
A
|
B
|
C
```

Nodes are explored level by level using a queue.

---

## Message Queues

Systems like:

- RabbitMQ
- Kafka
- AWS SQS

use queue concepts.

---

# Why Not Use a List?

Python:

```python
queue = []
```

Dequeue:

```python
queue.pop(0)
```

Complexity:

```text
O(n)
```

because all elements shift.

Not efficient.

---

# Use deque Instead

Python:

```python
from collections import deque
```

Create:

```python
queue = deque()
```

Both ends become efficient.

---

# Queue Operations

## Enqueue

Add to rear.

```python
queue.append(x)
```

Example:

```python
queue.append(10)
```

Queue:

```text
10
```

Complexity:

```text
O(1)
```

---

## Dequeue

Remove from front.

```python
queue.popleft()
```

Example:

```text
10 20 30
```

After:

```python
queue.popleft()
```

Queue:

```text
20 30
```

Complexity:

```text
O(1)
```

---

## Front Element

```python
queue[0]
```

Example:

```text
10 20 30
```

Output:

```python
10
```

Complexity:

```text
O(1)
```

---

## Rear Element

```python
queue[-1]
```

Example:

```text
10 20 30
```

Output:

```python
30
```

Complexity:

```text
O(1)
```

---

# Python Queue Implementation

```python
from collections import deque

queue = deque()

queue.append(1)

queue.append(2)

queue.append(3)

print(queue)
```

Output:

```python
deque([1, 2, 3])
```

---

Dequeue:

```python
queue.popleft()
```

Output:

```python
deque([2, 3])
```

---

Front:

```python
print(queue[0])
```

Output:

```python
2
```

---

# Java Queue

```java
import java.util.Queue;
import java.util.LinkedList;

Queue<Integer> queue =
    new LinkedList<>();

queue.offer(1);

queue.offer(2);

queue.offer(3);

queue.poll();

queue.peek();
```

---

# Complexity Summary

| Operation | Complexity |
|------------|------------|
| Enqueue | O(1) |
| Dequeue | O(1) |
| Front | O(1) |
| Rear | O(1) |

---

# Queue Visualization

```text
Front                Rear

1   2   3   4   5

Remove Here →
```

After dequeue:

```text
Front          Rear

2   3   4   5
```

---

# Common Mistakes

## Mistake 1

Using:

```python
list.pop(0)
```

instead of:

```python
deque.popleft()
```

---

## Mistake 2

Confusing Queue and Stack.

Queue:

```text
FIFO
```

Stack:

```text
LIFO
```

---

## Mistake 3

Using:

```python
pop()
```

instead of:

```python
popleft()
```

when implementing queues.

---

# When Should You Think Queue?

Big interview clues:

```text
Level Order

Breadth First Search

First Come First Serve

Scheduling

Waiting Line

Shortest Path (Unweighted Graph)
```

Whenever you see these clues:

```text
Think Queue
```

---

# Queue Cheat Sheet

```python
from collections import deque

queue = deque()

queue.append(x)     # Enqueue

queue.popleft()     # Dequeue

queue[0]            # Front

queue[-1]           # Rear
```

---

# Problems We'll Solve

### Easy

1. Implement Queue Using Stacks (#232)

### Medium

2. Number of Recent Calls (#933)
3. Rotting Oranges (#994)
4. Binary Tree Level Order Traversal (#102)

### Advanced

5. Word Ladder (#127)
6. Shortest Path in Binary Matrix (#1091)

---

# Key Takeaways

✅ Queue follows FIFO

✅ First inserted = first removed

✅ Use `deque` in Python

✅ `append()` = enqueue

✅ `popleft()` = dequeue

✅ O(1) operations

✅ Foundation of BFS and scheduling problems

---

# Golden Rule Learned

```text
Need First Come
First Serve?
      ↓
   Use Queue
```

Queues are the backbone of BFS, scheduling systems, and many real-world software architectures.
