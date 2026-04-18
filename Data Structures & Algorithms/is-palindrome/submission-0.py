class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i = 0
        j = len(s) - 1
        while i < j:
            left_char = s[i]
            right_char = s[j]
            if not left_char.isalnum():
                i += 1
                continue
            if not right_char.isalnum():
                j -= 1
                continue

            if left_char.lower() == right_char.lower():
                i += 1
                j -= 1
            else:
                return False
        return True