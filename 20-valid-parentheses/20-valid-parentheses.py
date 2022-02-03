class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        hash_map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for char in s:
            if char in hash_map:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                open_tag = stack.pop()
                if hash_map[open_tag] != char:
                    return False
        return len(stack) == 0