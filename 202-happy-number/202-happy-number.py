class Solution:
    def isHappy(self, n: int) -> bool:
        
        visit = set()
        
        while n not in visit:
            
            visit.add(n)
            n = self.sumOfSquares(n)
            
            if n == 1: return True
            
        return False
    
    def sumOfSquares(self, n):
        
        new_n = 0
        for i in str(n):
            new_n += (int(i) ** 2)
        return new_n
            
        

            
        
        