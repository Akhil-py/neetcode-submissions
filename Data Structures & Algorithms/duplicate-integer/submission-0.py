class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = {}
        for i in nums:
            if i in unique:
                unique[i] += 1
            else:
                unique[i] = 1
            if unique[i] > 1:
                return True
        return False