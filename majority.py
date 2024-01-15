class solution:
    def majority(self,nums:[])->int:
        count=0
        cand=0
        n=len(nums)
        for i in range(n-1):
            if count==0:
                cand=nums[i]
            if cand==nums[i]:
                count+=1
            else:
                count-=1
        return cand           
obj=solution()    
result=obj.majority([88,22,11,11])
print(result)