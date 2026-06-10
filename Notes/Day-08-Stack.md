# Class 8 — Stacks

## Why Stacks Matter

Stacks are one of the most important data structures in coding interviews.

Many medium and hard problems become simple once you recognize the Stack pattern.

Common interview topics include:

- Valid Parentheses
- Min Stack
- Monotonic Stack
- Next Greater Element
- Daily Temperatures
- Largest Rectangle in Histogram
- Expression Evaluation

---

# What is a Stack?

A Stack follows:

```text
LIFO

Last In
First Out
```

The last element inserted is the first element removed.

---

# Example

Operations:

```text
Push 1
Push 2
Push 3
```

Stack:

```text
Top
 ↓

3
2
1
```

---

Removing elements:

```text
Pop → 3

Pop → 2

Pop → 1
```

---

# Visualization

```text
Push 1

1

----------------

Push 2

2
1

----------------

Push 3

3
2
1

----------------

Pop

2
1

----------------

Pop

1
```

---

# Real World Examples

## Browser Back Button

Visit:

```text
Google
YouTube
GitHub
```

Stack:

```text
GitHub
YouTube
Google
```

Press Back:

```text
GitHub removed
```

Go to:

```text
YouTube
```

---

## Undo Operation

Type:

```text
A
B
C
```

Stack:

```text
C
B
A
```

Undo:

```text
Remove C
```

---

## Function Calls

When functions call other functions:

```python
main()

main()
 └─ funcA()

funcA()
 └─ funcB()
```

The Call Stack tracks execution.

---

## Parentheses Matching

Example:

```text
({[]})
```

The most recent opening bracket must close first.

Perfect Stack use case.

---

# Stack Operations

## Push

Add an element.

Python:

```python
stack.append(10)
```

Visualization:

```text
Before

5
3

After Push(10)

10
5
3
```

Complexity:

```text
O(1)
```

---

## Pop

Remove top element.

Python:

```python
stack.pop()
```

Visualization:

```text
Before

10
5
3

After Pop

5
3
```

Complexity:

```text
O(1)
```

---

## Peek / Top

View top element.

Python:

```python
stack[-1]
```

Visualization:

```text
Top

10
5
3
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

## Check Empty

Python:

```python
len(stack) == 0
```

or

```python
if not stack:
```

Complexity:

```text
O(1)
```

---

# Python Stack Implementation

```python
stack = []

stack.append(1)

stack.append(2)

stack.append(3)

print(stack)
```

Output:

```python
[1, 2, 3]
```

---

Remove:

```python
stack.pop()
```

Output:

```python
[1, 2]
```

---

Top:

```python
print(stack[-1])
```

Output:

```python
2
```

---

# Java Stack

```java
import java.util.Stack;

Stack<Integer> stack =
    new Stack<>();

stack.push(1);

stack.push(2);

stack.push(3);

stack.pop();

stack.peek();
```

---

# Arrays vs Stacks

| Feature | Array | Stack |
|----------|--------|--------|
| Access Random Index | O(1) | Not Intended |
| Push End | O(1) | O(1) |
| Pop End | O(1) | O(1) |
| LIFO Behavior | No | Yes |
| Peek Top | O(1) | O(1) |

---

# When Should You Think Stack?

Big interview clues:

```text
Most Recent Item

Undo

Reverse Order

Nested Structure

Matching Symbols

Previous Element

Next Greater Element
```

Whenever you see these clues:

```text
Think Stack
```

---

# Common Mistakes

## Mistake 1

Pop From Empty Stack

Wrong:

```python
stack.pop()
```

when:

```python
stack = []
```

Error occurs.

Always check:

```python
if stack:
```

---

## Mistake 2

Using Queue Logic

Stack:

```text
Last In First Out
```

Queue:

```text
First In First Out
```

Don't confuse them.

---

## Mistake 3

Forgetting Top Element

Many problems require:

```python
stack[-1]
```

before popping.

---

# Stack Complexity Summary

| Operation | Complexity |
|------------|------------|
| Push | O(1) |
| Pop | O(1) |
| Peek | O(1) |
| Empty Check | O(1) |

---

# Pattern Recognition

Whenever you hear:

- Undo
- Back Button
- Matching Parentheses
- Recent History
- Nested Structure
- Previous Element

Think:

```text
Stack
```

---

# Problems We'll Solve

### Easy

1. Valid Parentheses (#20)
2. Baseball Game (#682)
3. Min Stack (#155)

### Medium

4. Daily Temperatures (#739)
5. Next Greater Element (#496)
6. Evaluate Reverse Polish Notation (#150)

### Hard

7. Largest Rectangle in Histogram (#84)

---

# Key Takeaways

✅ Stack follows LIFO

✅ Push inserts at top

✅ Pop removes from top

✅ Peek views top

✅ All major operations are O(1)

✅ Perfect for recent-history problems

✅ Extremely common in interviews

---

# Golden Rule Learned

```text
Need The Most Recent Item?
            ↓
         Use Stack
```

Stacks are one of the easiest data structures to learn and one of the most powerful tools for solving interview problems.
