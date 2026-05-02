class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) solution after watching neetcode video: https://www.youtube.com/watch?v=P6RZZMu_maU
        set(nums)
        longest_streak = 0

        for i in nums:
            curr_streak = 0
            if i-1 in nums:
                continue
            j = i
            while j in nums:
                curr_streak += 1
                j += 1
            longest_streak = max(longest_streak, curr_streak)

        return longest_streak
