class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join([ch for ch in s if (ch.isalnum())]).lower()
        r = len(new_s) - 1
        for l in range(len(new_s)):
            if new_s[l] != new_s[r]:
                return False
            r -= 1
        return True
        