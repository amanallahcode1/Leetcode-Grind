class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ''.join(c for c in s if c.isalnum() == True).lower()
        rev = reversed(s_new)
        reversed_string = ''.join(rev)
        return reversed_string == s_new
    
        