class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Naive O(n log n) solution

        if len(nums) == 0:
            return 0

        nums.sort()
        prev = nums[0]
        curr_streak = 1
        longest_streak = 1

        print(nums)

        for i in nums:
            if i == prev:
                prev = i
                continue
            if i == prev + 1:
                curr_streak += 1
            else:
                longest_streak = max(curr_streak, longest_streak)
                curr_streak = 1
            prev = i

        longest_streak = max(curr_streak, longest_streak)
        return longest_streak


        
