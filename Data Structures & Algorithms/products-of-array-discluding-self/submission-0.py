class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # First attempt using the division operator
        product = 1
        output = []
        zero_count = 0

        for i in nums:
            if i == 0:
                zero_count += 1
            else:
                product *= i
        
        if zero_count > 1:
            return [0] * len(nums)
        
        for i in nums:
            if zero_count > 0:
                if i == 0:
                    output.append(product)
                else:
                    output.append(0)
            else:
                output.append(int(product/i))

        return output