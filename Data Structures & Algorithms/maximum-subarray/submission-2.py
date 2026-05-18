class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        window = nums[0]
        left = 0
        right = 1

        while right < len(nums):
            if nums[right] > window and window < 0:
                left = right
                window = nums[right]
            else:
                window += nums[right]
            right += 1
            maxSum = max(window, maxSum)

        return maxSum