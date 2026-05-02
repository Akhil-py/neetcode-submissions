class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) 

        for i in strs:
            vocab = [0] * 26

            for c in i:
                vocab[ord(c) - ord("a")] += 1

            res[tuple(vocab)].append(i)

        return list(res.values())