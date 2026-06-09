# LeetCode #344 — Reverse String

**Difficulty:** Easy

---

# Problem

Write a function that reverses a string.

The input is given as an array of characters.

You must modify the array **in-place** using O(1) extra memory.

---

## Example

### Input

```python
["h", "e", "l", "l", "o"]
```

### Output

```python
["o", "l", "l", "e", "h"]
```

---

# Key Observation

The first character should swap with the last.

The second character should swap with the second-last.

And so on.

Example:

```text
h  e  l  l  o
↑           ↑
Swap
```

After swap:

```text
o  e  l  l  h
```

Continue until pointers meet.

---

# Optimal Approach (Two Pointers)

Use:

```python
left = 0
right = len(s) - 1
```

While:

```python
left < right
```

Swap:

```python
s[left], s[right] = s[right], s[left]
```

Then move:

```python
left += 1
right -= 1
```

---

## Python Solution

```python
class Solution:
    def reverseString(self, s):

        left = 0
        right = len(s) - 1

        while left < right:

            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1
```

---

# Dry Run

Input:

```python
["h", "e", "l", "l", "o"]
```

Initial:

```python
left = 0
right = 4
```

---

### Iteration 1

```python
Swap:

h ↔ o
```

Array:

```python
["o", "e", "l", "l", "h"]
```

Move pointers:

```python
left = 1
right = 3
```

---

### Iteration 2

```python
Swap:

e ↔ l
```

Array:

```python
["o", "l", "l", "e", "h"]
```

Move pointers:

```python
left = 2
right = 2
```

Loop stops.

---

### Final Answer

```python
["o", "l", "l", "e", "h"]
```

---

# Visualization

```text
Initial

h  e  l  l  o
↑           ↑

Swap

o  e  l  l  h
   ↑     ↑

Swap

o  l  l  e  h
      ↑
```

Done ✅

---

# Why Does This Work?

Every swap places:

```text
One character
in its final position
from the left
```

and

```text
One character
in its final position
from the right
```

Therefore:

```text
Only n/2 swaps are needed.
```

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(1) |

### Why O(n)?

Each character is visited at most once.

Pointers move toward each other.

---

### Why O(1) Space?

No extra array is created.

Only two variables are used:

```python
left
right
```

---

# Java Solution

```java
class Solution {

    public void reverseString(char[] s) {

        int left = 0;
        int right = s.length - 1;

        while(left < right) {

            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;

            left++;
            right--;
        }
    }
}
```

---

# Interview Insight

This is one of the simplest and most important examples of:

## Opposite Direction Two Pointers

```text
left  ->      <-  right
```

Pointers start at opposite ends.

Move toward each other.

---

# Pattern Recognition

Whenever you hear:

- Reverse Array
- Reverse String
- Reverse Characters
- Swap Ends
- Mirror Elements

Think:

```text
Two Pointers
(Opposite Direction)
```

---

# Key Takeaways

✅ Reverse in-place

✅ Use two pointers

✅ Swap left and right elements

✅ Move pointers inward

✅ O(n) time

✅ O(1) extra space

✅ Classic Two Pointer interview problem

---

# Related Problems

1. Two Sum II
2. Valid Palindrome
3. Reverse Words in a String
4. Container With Most Water
5. Squares of a Sorted Array
6. Remove Duplicates from Sorted Array

All of these use the Two Pointer technique.

---

# Golden Rule Learned

```text
Need to process
both ends simultaneously?
        ↓
Use Two Pointers
```

Reverse String is the simplest example of the **Opposite Direction Two Pointer Pattern**.
