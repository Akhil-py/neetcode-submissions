class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        longest = 0
        seen = defaultdict(int)

        while right < len(s):
            seen[s[right]] += 1
            if seen[s[right]] > 1:
                longest = max(longest, right - left)
                while left < right and seen[s[right]] > 1:
                    seen[s[left]] -= 1
                    left += 1
            right += 1

        return max(longest, right - left)