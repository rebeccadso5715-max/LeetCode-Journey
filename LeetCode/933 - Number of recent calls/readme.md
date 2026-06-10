# LeetCode #933 — Number of Recent Calls

**Difficulty:** Easy

---

# Problem

Implement a counter that records recent requests.

A request is considered recent if it occurred within:

```text
[t - 3000, t]
```

milliseconds.

For every:

```python
ping(t)
```

return the number of requests inside that range.

---

## Example

### Input

```python
ping(1)
ping(100)
ping(3001)
ping(3002)
```

### Output

```python
1
2
3
3
```

---

# Understanding the Problem

For:

```python
ping(3002)
```

we keep requests inside:

```text
[2, 3002]
```

because:

```python
3002 - 3000 = 2
```

Requests:

```text
1
100
3001
3002
```

Remove:

```text
1
```

Keep:

```text
100
3001
3002
```

Count:

```python
3
```

---

# Key Observation

We only care about:

```text
Recent requests
```

Older requests become useless.

This is a huge clue.

Think:

```text
Queue
```

---

# Why Queue?

Requests arrive in order:

```text
1
100
3001
3002
```

The oldest request is always at the front.

When it becomes invalid:

```text
Remove from front
```

Perfect FIFO behavior.

---

# Visualization

```text
Queue

1
100
3001
3002
```

For:

```python
ping(3002)
```

Valid range:

```text
[2, 3002]
```

Remove:

```text
1
```

Queue becomes:

```text
100
3001
3002
```

Answer:

```python
3
```

---

# Optimal Approach

Use:

```python
deque
```

For every ping:

### Step 1

Add current request.

```python
q.append(t)
```

---

### Step 2

Remove expired requests.

```python
while q[0] < t - 3000:
    q.popleft()
```

---

### Step 3

Return current size.

```python
len(q)
```

---

# Python Solution

```python
from collections import deque

class RecentCounter:

    def __init__(self):

        self.q = deque()

    def ping(self, t):

        self.q.append(t)

        while self.q[0] < t - 3000:

            self.q.popleft()

        return len(self.q)
```

---

# Dry Run

### ping(1)

Queue:

```text
1
```

Range:

```text
[-2999, 1]
```

Count:

```python
1
```

---

### ping(100)

Queue:

```text
1
100
```

Range:

```text
[-2900, 100]
```

Count:

```python
2
```

---

### ping(3001)

Queue:

```text
1
100
3001
```

Range:

```text
[1, 3001]
```

Everything valid.

Count:

```python
3
```

---

### ping(3002)

Queue:

```text
1
100
3001
3002
```

Range:

```text
[2, 3002]
```

Remove:

```text
1
```

Queue:

```text
100
3001
3002
```

Count:

```python
3
```

---

# Full Visualization

```text
ping(1)

[1]

----------------

ping(100)

[1,100]

----------------

ping(3001)

[1,100,3001]

----------------

ping(3002)

[1,100,3001,3002]

Remove 1

[100,3001,3002]

Answer = 3
```

---

# Why Does This Work?

The queue always stores:

```text
Only valid requests
```

inside:

```text
[t-3000, t]
```

The front always contains:

```text
Oldest request
```

which is exactly what we need to remove.

---

# Complexity Analysis

| Operation | Complexity |
|------------|------------|
| ping() | O(1) amortized |
| Space | O(n) |

---

### Why O(1) Amortized?

Every request:

```text
Added once
Removed once
```

Although the while loop exists:

```python
while q[0] < t - 3000
```

each timestamp can only be removed one time.

Total work:

```text
O(n)
```

over all calls.

Therefore:

```text
O(1) amortized
```

per operation.

---

# Java Solution

```java
import java.util.LinkedList;
import java.util.Queue;

class RecentCounter {

    Queue<Integer> q;

    public RecentCounter() {

        q = new LinkedList<>();
    }

    public int ping(int t) {

        q.offer(t);

        while(q.peek() < t - 3000) {

            q.poll();
        }

        return q.size();
    }
}
```

---

# Interview Insight

This is one of the easiest Queue problems.

The key realization:

```text
Only keep useful elements.
```

As soon as an element becomes irrelevant:

```text
Remove it.
```

This idea appears everywhere.

---

# Pattern Recognition

Whenever you hear:

- Recent Events
- Last K Seconds
- Time Window
- Expiring Data
- Streaming Data

Think:

```text
Queue
```

or

```text
Sliding Window
```

---

# Common Mistakes

## Mistake 1

Using a list:

```python
pop(0)
```

Complexity:

```text
O(n)
```

Use:

```python
deque
```

instead.

---

## Mistake 2

Using:

```python
if
```

instead of:

```python
while
```

Multiple expired requests may exist.

---

## Mistake 3

Forgetting the range:

```text
[t - 3000, t]
```

It is inclusive.

---

# Queue Cheat Sheet

```python
from collections import deque

q = deque()

q.append(x)

q.popleft()

q[0]

len(q)
```

---

# Key Takeaways

✅ Requests arrive in order

✅ Queue stores timestamps

✅ Remove expired requests from front

✅ Keep only valid requests

✅ O(1) amortized per ping

✅ O(n) space

✅ Classic Queue + Sliding Window problem

---

# Related Problems

1. Implement Queue Using Stacks (#232)
2. Dota2 Senate (#649)
3. Moving Average from Data Stream (#346)
4. Sliding Window Maximum (#239)
5. Rotting Oranges (#994)

All involve processing data in arrival order.

---

# Golden Rule Learned

```text
Need To Track
Recent Elements?
        ↓
Use Queue
```

Number of Recent Calls is often the first problem that teaches how Queues and Sliding Windows work together.
