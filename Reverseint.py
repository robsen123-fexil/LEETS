class ReverseInt:
    def Solution(self, x:int)->int:
        y=str(x)
        z=list(y)
        nest=[]
        for i in range(len(z)-1,-1,-1):
            nest.append(z[i])

        nint=int(''.join(nest)) 
        nistr=str(nint)    
        nilist=list(nistr) 
        if nilist[0] =='0' :
            nilist.remove(nilist[0])
        nlast=int(''.join(nilist))   
        return nlast  
obj=ReverseInt()
result=obj.Solution(93)   
print(result)