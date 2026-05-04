class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + int((right - left)/2)

            if target == nums[mid]:
                # Target found
                return mid
            if nums[mid] >= nums[left]:
                # Left sorted side
                if target < nums[left]:
                    left = mid + 1
                elif target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right sorted side
                if nums[right] < target:
                    right = mid - 1
                elif target >= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
