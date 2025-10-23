class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        self= list(map(int, str(x)))
        n=len(self)
        for i in range(n//2):
            if self[i]!=self[-i-1]:
                 return False
        return True
    
    
    # without changing the input number into list 
    def palindromeNum(self, x: int) -> bool:
        if x<0:
            return False
        return str(x)==str(x)[::-1]