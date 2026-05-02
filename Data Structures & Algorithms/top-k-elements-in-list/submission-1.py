class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]
        output = []

        for i in nums:
            res[i] += 1
        
        for i in res:
            freq[res[i]].append(i)


        for i in range(len(freq) - 1, -1, -1):
            output += freq[i]
            k -= len(freq[i])
            if k == 0:
                return output
        return output