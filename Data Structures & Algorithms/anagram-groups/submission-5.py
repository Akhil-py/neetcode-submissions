class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # This solution was written after watching neetcode's video: https://www.youtube.com/watch?v=vzdNOK2oB2E
        # I did not look at the code while writing the following solution with two exceptions as stated in the inline comments
        
        res = defaultdict(list) # refered to solution for this datastructure

        for i in strs:
            vocab = [0] * 26

            for c in i:
                vocab[ord(c) - ord("a")] += 1

            res[tuple(vocab)].append(i)

        return list(res.values()) # refered to solution for this return typecast and hasmap value indexing