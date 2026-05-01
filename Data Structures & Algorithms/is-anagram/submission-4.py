class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_alphabet = {}
        t_alphabet = {}
        for i in s:
            if i not in s_alphabet:
                s_alphabet[i] = 0
            s_alphabet[i] += 1

        
        for i in t:
            if i not in t_alphabet:
                t_alphabet[i] = 0
            t_alphabet[i] += 1

        if s_alphabet == t_alphabet:
            return True
        else:
            return False
        