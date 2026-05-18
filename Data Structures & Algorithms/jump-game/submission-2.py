class Solution:
    # Solution after watching neetcode video
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        while goal > 0:
            prev = goal
            for i in range(1, goal + 1):
                if nums[goal - i] + (goal - i) >= goal:
                    goal -= i
                    break
            if goal == prev:
                return False
        return True