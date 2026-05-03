class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Trivial algorithm in O(n) time
        lowest = nums[0]
        for i in nums:
            if i < lowest:
                return i
            lowest = min(i, lowest)
        return lowest