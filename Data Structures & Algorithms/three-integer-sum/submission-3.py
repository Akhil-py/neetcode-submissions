class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a = -9999999999
        res = []
        nums.sort()

        i = 0
        while i < len(nums) - 2:
            if nums[i] == a:
                i += 1
                continue
            a = nums[i]
            left = i + 1
            right = len(nums) - 1
            while right > left:
                b = nums[left]
                c = nums[right]
                if a + b + c > 0:
                    right -= 1
                elif a + b + c < 0:
                    left += 1
                else:
                    res.append([a, b, c])
                    while left < right and nums[left] == b:
                        left += 1
                    while left < right and nums[right] == c:
                        right -= 1
            i += 1

        return res