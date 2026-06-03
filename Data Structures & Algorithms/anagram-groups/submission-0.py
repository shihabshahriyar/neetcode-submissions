class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = dict[str, List[str]]()
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in strs_dict:
                strs_dict[sorted_word].append(word)
            else:
                strs_dict[sorted_word] = [word]
        
        output = []
        for key, value in strs_dict.items():
            output.append(value)
        return output
        