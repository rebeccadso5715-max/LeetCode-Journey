# LeetCode #242 — Valid Anagram

**Difficulty:** Easy

---

# Problem

Given two strings `s` and `t`, return:

```text
True
```

if `t` is an anagram of `s`.

Otherwise return:

```text
False
```

An **anagram** is a word formed by rearranging the letters of another word while using all letters exactly once.

---

## Example

### Input

```python
s = "anagram"
t = "nagaram"
```

### Output

```python
True
```

### Explanation

Both strings contain:

```text
a → 3
n → 1
g → 1
r → 1
m → 1
```

Same character frequencies ⇒ Valid Anagram.

---

# Key Observation

Two strings are anagrams if:

```text
Every character appears
the same number of times
in both strings.
```

This is a classic:

```text
Frequency Counting
+
Hash Map
```

problem.

---

# Optimal Approach

Count character frequencies in the first string.

Then remove frequencies using the second string.

If anything becomes invalid:

```python
return False
```

Otherwise:

```python
return True
```

---

## Python Solution

```python
class Solution:
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:

            if ch not in count:
                return False

            count[ch] -= 1

            if count[ch] < 0:
                return False

        return True
```

---

# Dry Run

Input:

```python
s = "anagram"
t = "nagaram"
```

---

### Step 1: Count Frequencies

```python
count = {
    'a': 3,
    'n': 1,
    'g': 1,
    'r': 1,
    'm': 1
}
```

---

### Step 2: Process t

Character:

```python
'n'
```

```python
count['n'] = 0
```

Character:

```python
'a'
```

```python
count['a'] = 2
```

Character:

```python
'g'
```

```python
count['g'] = 0
```

Continue...

Final map:

```python
{
    'a': 0,
    'n': 0,
    'g': 0,
    'r': 0,
    'm': 0
}
```

All counts balanced ✅

Return:

```python
True
```

---

# Visualization

```text
String 1

a n a g r a m

↓

Frequency Map

a → 3
n → 1
g → 1
r → 1
m → 1

↓

Process String 2

n a g a r a m

↓

All counts become 0

↓

Valid Anagram
```

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(1)* |

### Why O(n)?

We traverse both strings once.

---

### Why O(1) Space?

Only lowercase English letters exist.

Maximum unique characters:

```text
26
```

A constant amount of storage.

Technically:

```text
O(26) = O(1)
```

---

# Alternative Python Solution

Using Counter:

```python
from collections import Counter

class Solution:
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)
```

---

# Java Solution

```java
import java.util.HashMap;

class Solution {

    public boolean isAnagram(String s, String t) {

        if(s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> count = new HashMap<>();

        for(char ch : s.toCharArray()) {
            count.put(ch,
                count.getOrDefault(ch, 0) + 1);
        }

        for(char ch : t.toCharArray()) {

            if(!count.containsKey(ch)) {
                return false;
            }

            count.put(ch, count.get(ch) - 1);

            if(count.get(ch) < 0) {
                return false;
            }
        }

        return true;
    }
}
```

---

# Interview Insight

This problem teaches:

```text
Frequency Counting
```

One of the most important Hash Map patterns.

Instead of storing positions:

```text
Character → Count
```

---

# Pattern Recognition

Whenever you hear:

- Anagram
- Character Frequency
- Count Letters
- Same Characters
- Rearrangement

Think:

```text
Hash Map
+
Frequency Counting
```

---

# Key Takeaways

✅ Anagrams have identical character frequencies

✅ Hash Maps are perfect for counting

✅ Count characters in first string

✅ Remove counts using second string

✅ If all counts balance, strings are anagrams

✅ Classic frequency-counting interview problem

---

# Related Problems

1. Contains Duplicate
2. Group Anagrams
3. Ransom Note
4. Find All Anagrams in a String
5. Top K Frequent Elements
6. Majority Element

All of these use the Frequency Counting pattern.
