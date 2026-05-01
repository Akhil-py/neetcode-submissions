class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = []

        for i in nums:
            sorted_nums.append(i)
        
        sorted_nums.sort()

        left = 0
        right = len(sorted_nums) - 1

        while left < right: 
            if sorted_nums[left] + sorted_nums[right] > target:
                right -= 1
            elif sorted_nums[left] + sorted_nums[right] < target:
                left += 1
            else:
                indexes = []
                for i in range(len(nums)):
                    if nums[i] in [sorted_nums[left], sorted_nums[right]]:
                        indexes.append(i)
                return indexes
