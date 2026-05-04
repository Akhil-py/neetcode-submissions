class Solution:
    def minWindow(self, s: str, t: str) -> str:
        vocab = {}
        window = {}
        have = 0
        need = 0
        shortest_length = len(s)
        shortest_string = ""
        left, right = 0, 0

        if s == t:
            return s
        if t == "" or s == "" or len(t) > len(s):
            return ""

        for c in t:
            if c not in vocab:
                vocab[c] = 0
                window[c] = 0
                need += 1
            vocab[c] += 1
        
        while right < len(s):
            if s[right] in window:
                window[s[right]] += 1
                if window[s[right]] == vocab[s[right]]:
                    have += 1

            while have == need:
                if right - left < shortest_length:
                    shortest_length = right - left
                    shortest_string = s[left:right+1]
                if s[left] in window:
                    window[s[left]] -= 1
                    if window[s[left]] < vocab[s[left]]:
                        have -= 1
                left += 1
            right += 1
        
        return shortest_string
