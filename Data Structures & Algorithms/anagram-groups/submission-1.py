class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = set()
        output = []

        for i in range(len(strs)):
            block = []
            curr_word = {}


            if i in seen:
                continue
            
            block.append(strs[i])
            seen.add(i)
            
            for x in strs[i]:
                if x not in curr_word:
                    curr_word[x] = 0
                curr_word[x] += 1

            for j in range(i+1, len(strs)):

                if j in seen:
                    continue
                
                word = {}
                for k in strs[j]:
                    if k not in word:
                        word[k] = 0
                    word[k] += 1

                if word == curr_word:
                    block.append(strs[j])
                    seen.add(j)
            
            if len(block) > 0:
                output.append(block)
        
        return output