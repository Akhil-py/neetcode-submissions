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
        
        print(s_alphabet)
        print(t_alphabet)
        if s_alphabet == t_alphabet:
            return True
        else:
            return False
        for i in s_alphabet:
            if i not in t_alphabet or s_alphabet[i] != t_alphabet[i]:
                return False
        
        return True