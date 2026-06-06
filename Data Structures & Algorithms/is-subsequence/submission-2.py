class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        left = 0

        for i in range(len(t)):
            if t[i] == s[left]:
                left += 1
            if left >= len(s):
                return True
        return False