class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]

        for i in strs:
            if len(i) == 0:
                return ""
            for j in range(len(i)):
                if j >= len(longest) or longest[j] != i[j]:
                    longest = longest[0:j]
                    continue
                elif j >= len(i) - 1:
                    longest = longest[0:j+1]
        return longest