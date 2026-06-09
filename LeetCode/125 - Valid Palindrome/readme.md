# LeetCode #125 — Valid Palindrome

**Difficulty:** Easy

---

# Problem

Given a string `s`, determine whether it is a palindrome.

A palindrome reads the same forward and backward after:

- Converting all uppercase letters to lowercase.
- Removing all non-alphanumeric characters.

---

## Example

### Input

```python
"A man, a plan, a canal: Panama"
```

### Output

```python
True
```

### Explanation

After removing spaces and punctuation:

```text
amanaplanacanalpanama
```

Forward:

```text
amanaplanacanalpanama
```

Backward:

```text
amanaplanacanalpanama
```

They are identical ✅

---

# Brute Force Approach

## Idea

1. Remove all non-alphanumeric characters.
2. Convert everything to lowercase.
3. Reverse the string.
4. Compare both strings.

---

## Python Solution

```python
class Solution:
    def isPalindrome(self, s):

        filtered = ""

        for ch in s:
            if ch.isalnum():
                filtered += ch.lower()

        return filtered == filtered[::-1]
```

---

# Dry Run

Input:

```python
"A man, a plan, a canal: Panama"
```

Filtered:

```python
"amanaplanacanalpanama"
```

Reverse:

```python
"amanaplanacanalpanama"
```

Comparison:

```python
True
```

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(n) |

### Why O(n) Space?

A new string is created.

---

# Optimal Approach (Two Pointers)

Instead of creating a new string:

- Use two pointers.
- Skip invalid characters.
- Compare characters directly.

This avoids extra space.

---

## Key Idea

Use:

```python
left = 0
right = len(s) - 1
```

Move inward.

Ignore:

```python
spaces
punctuation
special characters
```

Compare only:

```python
letters
digits
```

---

## Python Solution

```python
class Solution:
    def isPalindrome(self, s):

        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
```

---

# Dry Run

Input:

```python
"A man, a plan, a canal: Panama"
```

Initial:

```python
left = 0
right = len(s)-1
```

---

### Compare

```python
A ↔ a
```

After lowercase:

```python
a == a
```

Move pointers.

---

### Skip Spaces

```python
" "
","
":"
```

Pointers automatically skip them.

---

### Continue Comparing

```python
m ↔ m
a ↔ a
n ↔ n
...
```

All comparisons succeed.

Return:

```python
True
```

---

# Visualization

```text
A man, a plan, a canal: Panama
↑                           ↑

A == a

Move inward

  ↑                       ↑

m == m

Move inward

Skip spaces and punctuation

Continue...
```

Eventually:

```text
All characters match
```

Return:

```python
True
```

---

# Why Does This Work?

A palindrome requires:

```text
First character = Last character
Second character = Second-last character
...
```

Two pointers naturally compare mirrored positions.

---

# Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time | O(n) |
| Space | O(1) |

### Why O(n)?

Each character is processed at most once.

---

### Why O(1) Space?

No extra string is created.

Only:

```python
left
right
```

are used.

---

# Java Solution

```java
class Solution {

    public boolean isPalindrome(String s) {

        int left = 0;
        int right = s.length() - 1;

        while(left < right) {

            while(left < right &&
                  !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }

            while(left < right &&
                  !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }

            if(Character.toLowerCase(s.charAt(left))
               != Character.toLowerCase(s.charAt(right))) {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }
}
```

---

# Interview Insight

This problem teaches:

## Opposite Direction Two Pointers

```text
left  ->      <- right
```

But with an extra twist:

```text
Skip unwanted characters
```

This pattern appears frequently in string problems.

---

# Pattern Recognition

Whenever you hear:

- Palindrome
- Compare Ends
- Mirror Characters
- Ignore Spaces
- Ignore Punctuation

Think:

```text
Two Pointers
```

---

# Key Takeaways

✅ Palindromes compare mirrored characters

✅ Two pointers are ideal for comparing ends

✅ Skip non-alphanumeric characters

✅ Compare lowercase versions

✅ O(n) time

✅ O(1) extra space

✅ Classic string interview problem

---

# Related Problems

1. Reverse String
2. Two Sum II
3. Valid Palindrome II
4. Palindromic Substrings
5. Longest Palindromic Substring
6. Reverse Words in a String

All of these involve Two Pointer thinking.

---

# Golden Rule Learned

```text
Need to compare
characters from both ends?
        ↓
Use Two Pointers
```

Valid Palindrome is one of the most important Two Pointer string problems and is frequently asked in interviews.
