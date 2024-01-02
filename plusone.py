class solution:
    def plusone(self,digits:list)->list:
        num=int(''.join(map(str,digits)))
        num+=1
        nums=list(map(int,str(num)))
        return nums
obj=solution()
result=obj.plusone([3,5,9])    
print(result)