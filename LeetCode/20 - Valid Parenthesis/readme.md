# LeetCode #20 — Valid Parentheses

**Difficulty:** Easy

---

# Problem

Given a string containing:

```text
(
)
[
]
{
}
```

Determine whether the parentheses are valid.

Return:

```python
True
```

if valid.

Otherwise:

```python
False
```

---

## Example 1

### Input

```python
s = "()"
```

### Output

```python
True
```

---

## Example 2

### Input

```python
s = "()[]{}"
```

### Output

```python
True
```

---

## Example 3

### Input

```python
s = "(]"
```

### Output

```python
False
```

---

## Example 4

### Input

```python
s = "([)]"
```

### Output

```python
False
```

---

# Key Observation

Every opening bracket must be closed by:

```text
( → )

[ → ]

{ → }
```

And:

```text
The most recently opened bracket
must be closed first.
```

This is exactly:

```text
LIFO
(Last In First Out)
```

which means:

```text
Stack
```

---

# Brute Force Thinking

Repeatedly remove:

```text
()
[]
{}
```

until nothing remains.

Example:

```text
([{}])

↓

([])

↓

()

↓

""
```

Valid.

---

Problem:

Repeated scanning.

Complexity becomes large.

Not efficient.

---

# Why Stack?

Consider:

```text
([{}])
```

Open brackets:

```text
(
[
{
```

The last opened bracket:

```text
{
```

must close first.

Stack naturally handles this.

---

# Visualization

Input:

```text
([{}])
```

---

### Push (

```text
(
```

---

### Push [

```text
[
(
```

---

### Push {

```text
{
[
(
```

---

### Read }

Top:

```text
{
```

Match.

Pop.

```text
[
(
```

---

### Read ]

Top:

```text
[
```

Match.

Pop.

```text
(
```

---

### Read )

Top:

```text
(
```

Match.

Pop.

```text
Empty
```

Valid.

---

# Optimal Approach

Use:

```python
stack
```

and a mapping:

```python
{
 ')': '(',
 '}': '{',
 ']': '['
}
```

Whenever we see a closing bracket:

```python
)
```

we check whether the top of stack contains:

```python
(
```

---

# Python Solution

```python
class Solution:
    def isValid(self, s):

        stack = []

        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:

            if ch in mapping:

                if not stack:
                    return False

                top = stack.pop()

                if top != mapping[ch]:
                    return False

            else:
                stack.append(ch)

        return len(stack) == 0
```

---

# Dry Run

Input:

```python
"()[]{}"
```

---

### Read (

Push:

```text
(
```

---

### Read )

Pop:

```text
(
```

Matches.

Stack:

```text
Empty
```

---

### Read [

Push:

```text
[
```

---

### Read ]

Pop:

```text
[
```

Matches.

---

### Read {

Push:

```text
{
```

---

### Read }

Pop:

```text
{
```

Matches.

---

Final Stack:

```text
Empty
```

Return:

```python
True
```

---

# Example of Invalid Case

Input:

```python
"([)]"
```

---

### Push (

```text
(
```

---

### Push [

```text
[
(
```

---

### Read )

Expected:

```text
(
```

Top:

```text
[
```

Mismatch.

Return:

```python
False
```

---

# Why Return

```python
len(stack) == 0
```

?

Consider:

```python
"((("
```

No mismatch occurs.

But:

```text
Three brackets remain open.
```

Stack:

```text
(
(
(
```

Not empty.

Invalid.

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(n) |

### Why O(n)?

Each character is:

```text
Pushed once
Popped once
```

---

### Why O(n) Space?

Worst case:

```python
"((((((((("
```

All characters stored in stack.

---

# Java Solution

```java
import java.util.Stack;
import java.util.HashMap;

class Solution {

    public boolean isValid(String s) {

        Stack<Character> stack =
            new Stack<>();

        HashMap<Character, Character>
            mapping = new HashMap<>();

        mapping.put(')', '(');
        mapping.put('}', '{');
        mapping.put(']', '[');

        for(char ch : s.toCharArray()) {

            if(mapping.containsKey(ch)) {

                if(stack.isEmpty()) {
                    return false;
                }

                char top = stack.pop();

                if(top != mapping.get(ch)) {
                    return false;
                }
            }

            else {
                stack.push(ch);
            }
        }

        return stack.isEmpty();
    }
}
```

---

# Interview Insight

This is the most important beginner Stack problem.

The key realization:

```text
Closing Bracket
Needs Most Recent
Opening Bracket
```

That's exactly:

```text
Stack
```

---

# Pattern Recognition

Whenever you hear:

- Matching Symbols
- Nested Structure
- Open / Close
- Undo
- Most Recent Item

Think:

```text
Stack
```

---

# Common Mistakes

## Mistake 1

Doing:

```python
stack.pop()
```

without checking:

```python
if not stack
```

May cause error.

---

## Mistake 2

Comparing:

```python
')' == '('
```

instead of using mapping.

---

## Mistake 3

Returning:

```python
True
```

immediately after traversal.

Must verify:

```python
stack is empty
```

---

# Stack Cheat Sheet

```python
stack.append(x)   # Push

stack.pop()       # Pop

stack[-1]         # Top

len(stack) == 0   # Empty
```

---

# Key Takeaways

✅ Matching brackets follow LIFO order

✅ Stack is the perfect data structure

✅ Push opening brackets

✅ Match closing brackets

✅ Stack must be empty at the end

✅ O(n) time

✅ O(n) space

✅ One of the most famous Stack interview questions

---

# Related Problems

1. Baseball Game (#682)
2. Min Stack (#155)
3. Backspace String Compare (#844)
4. Daily Temperatures (#739)
5. Remove All Adjacent Duplicates (#1047)

All use Stack-based thinking.

---

# Golden Rule Learned

```text
Need To Match
Recent Open Symbol?
         ↓
      Use Stack
```

Valid Parentheses is the foundation of Stack pattern recognition and appears in countless interview variations.
