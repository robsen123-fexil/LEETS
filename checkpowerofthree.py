class solution:
    def powerofthree(self, n:int)->bool:
        while n>0:
            if n%3==2:
                return False
        return True    
         
      
obj=solution()
result=obj.powerofthree(21)
print(result)