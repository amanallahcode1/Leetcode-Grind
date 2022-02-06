class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_c = Counter('balloon')
        text_c = Counter(text)
        
        res = len(text)
        for char in balloon_c:
            res = min(res, text_c[char] // balloon_c[char])
        return res
        