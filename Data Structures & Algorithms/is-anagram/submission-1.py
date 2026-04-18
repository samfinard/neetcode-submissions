class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counter = {}
        t_counter = {}

        for char in s:
            if char in s_counter:
                s_counter[char] += 1
            else:
                s_counter[char] = 1
        
        for char in t:
            if char in s_counter:
                s_counter[char] -= 1
            else:
                return False
        
        for char in s_counter:
            if s_counter[char] != 0:
                return False

        return True