class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        output = []

        for i in nums:
            res[i] += 1
        
        res = list(sorted(res.items(), key=lambda x: x[1], reverse=True))
        for j in res[:k]:
            output.append(j[0])

        return output