class Solution:
    # Solution after watching neetcode video
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        while goal > 0:
            for i in range(1, goal + 1):
                if nums[goal - i] + (goal - i) >= goal:
                    goal -= i
                    break
            else:
                return False
        return True