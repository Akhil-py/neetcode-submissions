class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = ""
        encoded = ""
        for i in strs:
            lengths += str(len(i)) + "-"
            encoded += i
        encoded = lengths + "~" + encoded
        
        return encoded

    def decode(self, s: str) -> List[str]:
        i = -1
        lengths = []
        decoded = []
        curr_length = ""

        while i < len(s):
            i += 1
            if s[i] == "-":
                lengths.append(int(curr_length))
                curr_length = ""
                continue
            if s[i] == "~":
                s = s[i+1:]
                break
            
            curr_length += s[i]

        j = 0
        for length in lengths:
            word = ""
            for n in range(length):
                word += s[j]
                j += 1
            decoded.append(word)

        return decoded