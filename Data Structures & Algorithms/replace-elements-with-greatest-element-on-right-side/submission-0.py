class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ge = -1
        for i in range(len(arr) - 1, -1, -1):
            next_ge = max(ge, arr[i])
            arr[i] = ge
            ge = next_ge
        return arr

