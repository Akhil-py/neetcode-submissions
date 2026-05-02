class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Second attempt after watching neetcode's video: http://youtube.com/watch?v=bNvIQI2wAjk&t=368s
        prefix = 1
        postfix = 1
        output = [0] * len(nums)
        output[0] = 1

        for i in range(len(nums)):
            prefix *= nums[i]
            if i < len(nums) - 1:
                output[i+1] = prefix

        for i in range(len(nums) - 1, -1, -1):
            postfix *= nums[i]
            if i > 0:
                output[i-1] *= postfix
        
        return output