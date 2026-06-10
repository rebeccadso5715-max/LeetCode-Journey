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
