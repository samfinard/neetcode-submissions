class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {} # maps freq dict to list of string
        for s in strs:    
            freq_dict = self.get_frequency_dict(s)
            key = tuple(sorted(freq_dict.items()))
            if key in anagram_dict:
                anagram_dict[key].append(s)
            else:
                anagram_dict[key] = [s]
        return list(anagram_dict.values())

        
    
    
    def get_frequency_dict(self, s: str) -> Dict[str:int]:
        freq_dict = {}
        for char in s:
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
        return freq_dict