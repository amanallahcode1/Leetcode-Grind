from collections import Counter
class Solution:

    def rearrangeCharacters(self, s: str, target: str) -> int:
        
        countS, countTarget = Counter(s), Counter(target)
        numOfCopies = float('inf')
        
        for i in countTarget:
            numOfCopies = min(numOfCopies, countS[i] // countTarget[i])
        return numOfCopies
            
        