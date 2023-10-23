class Solution:
    def Palindrome(self, x: int) -> bool:
        y=str(x)
        rev=y[::-1]
        z=int(rev)
        if x<0:
            return False
        elif z==x:
         return True
        else :
         return False   
        
obj= Solution()
result=obj.Palindrome(-46)
print(result)
     
    
            