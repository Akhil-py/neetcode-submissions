class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        left = 0
        longest = 0
        duplicates = 0

        for i in range(len(s)):
            seen[s[i]] += 1
            duplicates += 1
            while left < i and k - duplicates + max(seen.values()) < 0:
                longest = max(longest, i - left)
                seen[s[left]] -= 1
                duplicates -= 1
                left += 1
        
        return max(longest, len(s) - left)