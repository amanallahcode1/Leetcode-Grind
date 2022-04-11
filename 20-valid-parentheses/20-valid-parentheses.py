class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
       # hash_map {(: ), {:}, }
       # if i find open tag:
        # add hash_map[open], (which is closing tag) to stack
        # if i find closing tag:
            # pop from stack:
            # if they dont match return false
        
    # if by end: stack is empty: return true
    
        close_open = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        stack = []
        
        for i in s:
            if i in close_open:
                stack.append(close_open[i])
            else:
                if stack and stack[-1] == i:
                    stack.pop()
                else:
                    return False
                
        return True if not stack else False
        
                