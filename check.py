
def check(a):
         i=0
         sub=[]
         print(a[i])
         print(a[i:i+1])
         while i<len(a):
              sub.append(a[i:i+2])
              
          
         return sub
arr=[12,33,44]
result=check(arr)
print(result)      