class solution:
    def stock(self , price:list)->int:
        idn=price.index(min(price))
        res=[]
        print(idn)
        for i in range(idn,len(price)):
            res.append(price[i])
        print(res)
        
        lr=res.index(max(res))   
        return lr
obj=solution()
result=obj.stock([9,3,89,7,10,6])    
print(result)