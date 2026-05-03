class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Optimized binary search algorithm in O(log n) time
        low = 0
        high = len(nums) - 1
        minimum = 3000
        

        while low <= high:
            midpoint = low + int((high - low) / 2)
            minimum = min(minimum, nums[midpoint])
            if nums[midpoint] >= nums[low] and nums[midpoint] > nums[high]:
                low = midpoint + 1
            else:
                high = midpoint - 1

        return minimum