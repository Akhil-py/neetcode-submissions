class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            if not ((ord(s[left].lower()) >= ord('a') and ord(s[left].lower()) <= ord('z')) or (ord(s[left].lower()) >= ord('0') and ord(s[left].lower()) <= ord('9'))):
                left += 1
                continue
            if not ((ord(s[right].lower()) >= ord('a') and ord(s[right].lower()) <= ord('z')) or (ord(s[right].lower()) >= ord('0') and ord(s[right].lower()) <= ord('9'))):
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True