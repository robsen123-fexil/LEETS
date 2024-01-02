class solution:
    def powerofthree(self, n:int)->bool:
        if  n>0:
            if n%3==2:
                return False
            else:
                return True
obj=solution()
result=obj.powerofthree(91)
print(result)