class Solution:
    def isValid(self, s: str) -> bool:
        # Optimized Neetcode solution from video: https://www.youtube.com/watch?v=WTzjTskDFMg
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return False if stack else True

        